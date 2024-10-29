function getAverageAge(list) {
    let count=0  //count represents the number of developers
    let sumAges=0
    list.forEach((dev)=>{
      count++
      sumAges+=dev.age})
    return Math.round(sumAges/count)
    
  }