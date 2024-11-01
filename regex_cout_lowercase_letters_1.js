function lowercaseCount(str){
    var matches = str.match(/[a-z]/g)
    return matches ? matches.length : 0
  }