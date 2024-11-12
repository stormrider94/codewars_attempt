function positiveSum(arr) {
    let sumPositive=0
    if(arr===null) return sumPositive
  arr.forEach((number)=>{
    if(number>0) sumPositive+=number
  }) 
    return sumPositive
    
  }