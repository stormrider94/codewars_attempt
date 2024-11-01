function reverse(string){
    var words_li = string.split(/[\s]+/)
    words_li.reverse()
    return words_li.join(" ")
  }