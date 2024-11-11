function sortByLanguage(list) {
    let sortedDevs=list.sort(function(a,b){
      let langA=a.language.toUpperCase()
      let langB=b.language.toUpperCase()
      let nameA=a.firstName.toUpperCase()
      let nameB=b.firstName.toUpperCase()
      if(langA<langB)return -1
      if(langA>langB)return 1
      else if(langA===langB&&nameA<nameB)return -1
      else if(langA===langB&&nameA>nameB)return 1
    })
    console.log(sortedDevs)
    return sortedDevs
    }