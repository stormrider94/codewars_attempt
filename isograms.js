function isIsogram(str){
  if(str===''){
    return true
  }
//   To ensure that the letter cases don't affect our function
  let safe = str.toLocaleLowerCase()
  //we create an array from the string.
  let stringArray = Array.from(safe)
  let duplicates = stringArray.filter((character,index)=>{
    if(stringArray.indexOf(character)!==index)  return character
      })
     if(duplicates.length!==0) return false
//     if there are duplicates in the array,it means there are repeating letters and the word is not an isogram                                
  else return true
  //meaning the length of duplicates array is zero and there are no dupicates whatsoever hence the word is an isogram
  
  }