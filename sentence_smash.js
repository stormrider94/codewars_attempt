function smash (words) {
    let sentence=""
    let length=words.length
    if(length===1) return words.join('')
    if(length===0)return ''
    words.forEach((word)=>{
      //they don't want space at the beginning of the sentence
      if(word===words[0]) sentence+= `${word} `
      //space isn't needed at the end of the word as well
      else if(word===words[length-1]){
        sentence+=`${word}`
      }else sentence +=`${word} `
      }) 
     return sentence
  };