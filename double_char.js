function doubleChar(str) {
    // Your code here
    let strArray=str.split('')
    let newArray=[]
    strArray.forEach((char)=>{
      newArray.push(char)
      newArray.push(char)    
    })
    let outputString=newArray.join("")
    console.log(outputString)
    return outputString
  }