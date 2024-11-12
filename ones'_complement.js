function onesComplement(n) {
    let complementArray=[]
    let arrayOfInput=Array.from(n.toString())
    arrayOfInput.forEach(element=>{
      if(element==="0"){
        complementArray.push('1')
        }
      else{
        complementArray.push('0')
      }
    })
  let answer= complementArray.join('')
  // gives us a string back
  return answer
  };