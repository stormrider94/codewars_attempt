function getEvenNumbers(numbersArray){
  let evenArray=numbersArray.filter(function(element){
     return element%2===0
  })
  return evenArray
  // filter out the odd numbers
}