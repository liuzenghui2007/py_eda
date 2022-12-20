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

datArray = []
for index, datFile in enumerate(datFiles):
    extractIndex = int(Path(datFile).stem[-3:])
    print(index, datFile, extractIndex)
    if index == extractIndex:
        dat = np.fromfile(datFile, dtype=np.float32)
        print(dat.shape)
        datArray.append(dat)
# datArray 是numpy array组成的list
datAll = np.concatenate(datArray, axis=0)
print('datAll', datAll.shape)
datReshape = np.reshape(datAll,(-1, activeChannelsLength + 1))
print('datReshape', datReshape.shape)
datA = datReshape[:,:-1] # 去掉mV通道
pyplot.plot(datA)
pyplot.show()