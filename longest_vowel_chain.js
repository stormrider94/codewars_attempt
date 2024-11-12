function solve(s){
    let regex = /[^aeiou]/gi
   let editedString = s.replace(regex," ")
   //replaces all extrawhitespace with just one whitespace
   editedString=editedString.replace(/\s+/gi," ")
  //   removes whiespace from the begining and the end
    editedString=editedString.trim()
   console.log(editedString)
    //create an array from the strings
    let vowelArray = editedString.split(" ")
    console.log(vowelArray)
    //create an array to store the length of each string
   let lengthArray= vowelArray.map(element=>element.length) 
  // we sort the length of the vowel strings from smallest to biggest
   lengthArray=lengthArray.sort(function(a,b){return a-b})
    const longestString = lengthArray.length-1
    console.log(lengthArray)
    //we return the largest string
    return lengthArray[longestString]
    
    
    }