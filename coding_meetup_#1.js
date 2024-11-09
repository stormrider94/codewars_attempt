function countDevelopers(list) {
    // your awesome code here :)
    let EuropeanJavaScriptDevs=list.filter(developerDetail=>{
     return developerDetail.continent==='Europe' && developerDetail.language==='JavaScript' 
    })
    return EuropeanJavaScriptDevs.length
  }