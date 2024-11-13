function findUniq(arr) {
    let arrayWithoutUnique=arr.filter((element,index)=>arr.indexOf(element)!==index)
    let set2= new Set(arrayWithoutUnique)
    let set= new Set(arr)
    let uniqueElements=[...set]
    let ultimateUnique=uniqueElements.filter(element=>{
      if(set2.has(element)){
        set.delete(element)
      }
      else{
        return element
      }
    })
    return Number(ultimateUnique.join())
  }