function twoSum(numbers, target) {
    //in coding it is a much better idea to keep things simple
    //we create the arr to store the pair
    let majestic=[]
    console.log(numbers)
    for(let i=0;i<numbers.length-1;i++){
      for(let j=i+1;j<numbers.length;j++){
        if(numbers[i]+numbers[j]===target){
          majestic.push(i)
          majestic.push(j)
          console.log(majestic)
          if(majestic.length==2){
             return majestic
            break
          }
        }
      }
    }
  }