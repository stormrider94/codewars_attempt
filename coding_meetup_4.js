function getFirstPython(list) {
    // Thank you for checking out my kata :)
    let firstPythonDev=list.find(dev=>{
     return dev.language==='Python'
    })
    console.log(firstPythonDev)
    if(firstPythonDev===undefined){
      return "There will be no Python developers"
    }else{
      return `${firstPythonDev.firstName}, ${firstPythonDev.country}`
    }
  }