function arrayDiff(a, b) {
    //we want to remove all values of a which are present in b
    //we also  want to remove all the occurences of the value present in b from it too
    //we will loop through b and if it has an element in a we delete it from tempArray
      for(let j=0;j<a.length;j++){
        for(let i=0;i<b.length;i++){
          if(a.indexOf(b[i])!==-1)a.splice(a.indexOf(b[i]),1)
        }
      }
    console.log(a)
    return a 
  }