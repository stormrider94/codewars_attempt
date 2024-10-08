function countWords(str) {
    str = str.trim()
    if(str.length == 0) {
      return 0
    }
    const words = str.split(/[\s]+/)
    const filteredWords = words.filter(word => word.length > 0);
    console.log(str," ",filteredWords)
    return filteredWords.length
  }