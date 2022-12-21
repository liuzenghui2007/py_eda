import numpy as np 
from pathlib import *
from matplotlib import pyplot

edhFile =  r"G:\polyseq\binary_file_py\e16data\20221108 eg4 N54 hepeslanmbda20K.edh"
edhContent = open(edhFile, 'r').readlines()
print('edhContent', edhContent)
activeChannels = edhContent[14].split(':')[1].strip().split(' ')
activeChannelsLength = len(activeChannels)
print('activeChannels', activeChannels)

edhName = Path(edhFile).stem
edhParent = Path(edhFile).parent
datFiles = [str(f) for f in Path(edhParent).glob(f"**\*.dat") if Path(f).is_file()]
print('edhName', edhName)
print('edhParent', edhParent)
print('datFiles', datFiles)

# dataArray是每一个dat文件的数据，拼成的list
dataArray = []
for index, datFile in enumerate(datFiles):
    extractIndex = int(Path(datFile).stem[-3:])
    print(index, datFile, extractIndex)
    if index == extractIndex:
        dat = np.fromfile(datFile, dtype=np.float32)
        print(dat.shape)
        dataArray.append(dat)
# dataAll是dataArray执行合并的结果
dataAll = np.concatenate(dataArray, axis=0)
print('dataArray', dataAll.shape)

# dataMatrix是dataAll转化成二维通道的结果
dataMatrix = np.reshape(dataAll,(-1, activeChannelsLength + 1))
print('dataMatrix', dataMatrix.shape)

# dataA是二维通道去掉最后一个电压通道的结果
dataA = dataMatrix[:,:-1] # 去掉mV通道
pyplot.plot(dataA)
pyplot.show()

np.save('data.npy', dataAll, allow_pickle=True, fix_imports=True)