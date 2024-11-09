function isLanguageDiverse(list) {
  // first of all we need to get the count of every language
  let languageCount={}
  list.forEach((dev)=>{
    if(dev.language in languageCount)languageCount[dev.language]++
    else languageCount[dev.language]=1
  })
//The language can't be more than 2 times higher than any of the other languages to be regarded as language-diverse.
    console.log(languageCount)
    if((languageCount.Python>2*languageCount.Ruby)||(languageCount.Python>2*languageCount.JavaScript))return false
    else if((languageCount.JavaScript>2*languageCount.Python)||(languageCount.JavaScript>2*languageCount.Ruby))return false
    else if((languageCount.Ruby>2*languageCount.JavaScript)||(languageCount.Ruby>2*languageCount.Python))return false
    else return true
  }