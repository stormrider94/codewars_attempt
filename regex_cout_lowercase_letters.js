function lowercaseCount(str){
    const all_matches = str.match(/[a-z]/g)
    if(all_matches) return all_matches.length
    else return 0
  }