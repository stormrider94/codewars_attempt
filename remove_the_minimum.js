function removeSmallest(numbers) {
    //goal is to rmove the smallest member from the array
  //   we first have to find the minimum without mutating the array
   let myNumbers=Array.from(numbers)
   let min=Math.min(...numbers)
   let minPosition=numbers.indexOf(min)
   myNumbers.splice(minPosition,1)
    return myNumbers
  }