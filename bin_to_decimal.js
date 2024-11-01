function binToDec(bin){
    let exponent= bin.length-1
    let numDeci=0
    let newBin=bin.split('')
    console.log(newBin)
    newBin.forEach((element)=>{
      numDeci+=Number(element)*(2**exponent)
      console.log(numDeci)
      exponent--
    })
   return numDeci
   }