function isPalindrome(x) {
    let caseSensitized=x.toLocaleLowerCase()
    let stringArray = caseSensitized.split('')
    let reversedArray = stringArray.reverse()
    let reversedString= reversedArray.join("")
    return caseSensitized===reversedString
  }