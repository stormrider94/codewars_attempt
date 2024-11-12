function getLargerNumbers(a, b) {
    let length=a.length
    //create an empty array 
   let newArray=[]
  for(i=0;i<length;i++){
      let x=a[i]
      let y=b[i]
      if(x>y){
        newArray.push(x)
      }else{
        newArray.push(y)
      }
  }
    
    console.log(newArray)
    return newArray;
  }