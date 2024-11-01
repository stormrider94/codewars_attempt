function mergeArrays(arr1, arr2) {
    let concatArray=arr1.concat(arr2)
    concatArray=concatArray.sort((a,b)=>a-b)
    concatArray=concatArray.filter((element,index)=>concatArray.indexOf(element)===index)
    return concatArray
  }