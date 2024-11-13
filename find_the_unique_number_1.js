function findUniq(arr) {
    let counter=0
    let nonDuplicatingArray = new Set(arr)
    nonDuplicatingArray=[...nonDuplicatingArray]
    let smallArr=arr.slice(0,4)
    for(let i=0;i<smallArr.length;i++){
    if(nonDuplicatingArray[0]===smallArr[i]){
    counter++
       }
    }
    if(counter===1){
      return nonDuplicatingArray[0]
    }
    else{
      return nonDuplicatingArray[1]
    }
    
  }