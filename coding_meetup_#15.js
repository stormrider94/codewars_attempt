function findOddNames(list) {
    let oddNames=list.filter((dev)=>{
      let sumcharcode=0
      for(i=0;i<dev.firstName.length;i++){
        sumcharcode+=dev.firstName.charCodeAt(i)
      }
      if(sumcharcode%2===1) return dev
    })
    return oddNames
  }