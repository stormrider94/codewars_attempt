function cubeOdd(arr) {
    if(arr.some((element)=>typeof(element)!=="number"))return undefined
    let sum=0
    arr.forEach((member)=>{
    if(member%2===1||member%2===-1){
      sum+=Math.pow(member,3)
    }})
    return sum
  }