function alternate(n, firstValue, secondValue){
    //please never use reserved words as variables
    let _switch = true
    let arr = []
    for(let i= 0;i<n;i++){
      if(_switch){
     arr.push(firstValue
     )}
      else{
        arr.push(secondValue)
      }
      _switch = !(_switch);
    }
    console.log(arr)
      return arr;
  }