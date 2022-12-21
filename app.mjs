import npyjs from "npyjs"

let n = new npyjs()

n.load("data.npy", (array, shape) => {
    // `array` is a one-dimensional array of the raw data
    // `shape` is a one-dimensional array that holds a numpy-style shape.
    console.log(
        `You loaded an array with ${array.length} elements and ${shape.length} dimensions.`
    );
});