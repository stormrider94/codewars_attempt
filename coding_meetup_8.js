function allContinents(list) {
    let continentList=['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
    list.forEach((dev)=>{
      /*if continentList has the developer's continent we want 
      to remove that continent from the array.
      */
      if(continentList.find(continent=>continent===dev.continent)){
        let indexPresent=continentList.indexOf(dev.continent)
        continentList.splice(indexPresent,1)
      }
    })
    console.log(continentList)
    /*if at the end of all the comparisons,there are still continents in the continent list Array
  this means not every continent has a representative so return false else return true*/
    if(continentList.length===0)return true
    else return false
  }