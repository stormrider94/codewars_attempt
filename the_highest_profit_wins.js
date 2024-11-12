function minMax(arr){
    let minmaxArr=[]
    minmaxArr.push(Math.min(...arr))
    minmaxArr.push(Math.max(...arr))
    return minmaxArr
  }