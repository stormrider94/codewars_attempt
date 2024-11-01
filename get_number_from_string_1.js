function getNumberFromString(s) {
    const num_from_str = s.replace(/[^\d]/g,"")
    console.log(num_from_str)
    return parseInt(num_from_str)
  }