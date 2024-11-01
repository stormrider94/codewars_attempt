function isLockNessMonster(s) {
    var pattern = /(three fifty)|(3.50)|(tree fiddy)/
    return pattern.test(s)
  }