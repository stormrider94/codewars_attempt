function getNumberFromString(s) {
    var pattern = /\D/g
    return Number(s.replace(pattern,""))
  }