function divisibleByThree(str){
    //   let numString=Number(str)
    //   console.log(numString)
      console.log(str.length)
      let numArray=str.split("")
      let jamelArray=numArray.map((value)=>{
        return Number(value)})
      console.log(jamelArray)
      let elliot= jamelArray.reduce((total,value)=>{
        return total+=value
      },0)
      console.log(typeof(elliot))
      if(elliot%3===0)return true
      else return false
    
    }