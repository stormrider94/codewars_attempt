function greetDevelopers(list) {
    // thank you for checking out my kata :)
    let newList=[]
    list.forEach((dev)=>{
      dev.greeting=`Hi ${dev.firstName}, what do you like the most about ${dev.language}?`
      newList.push(dev)
    })
    console.log(newList)
    return newList
  }