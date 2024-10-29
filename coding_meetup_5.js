function countLanguages(list) {
    // thank you for checking out the Coding Meetup kata :)
    //we create an empty object
    let countObject={}
     list.forEach((dev)=>{
       if(dev.language) countObject[`${dev.language}`]=0})
    //we get the languages present
    let languagesPresent=Object.keys(countObject)
  for(j=0;j<languagesPresent.length;j++){
    for(i=j;i<list.length;i++){
      if(languagesPresent[j]===list[i].language){
        console.log(list[i].language)
        countObject[list[i].language]++
      }
    }
  }
    console.log(countObject)
    return countObject
  }     