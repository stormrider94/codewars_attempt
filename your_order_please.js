function order(words){
    let stringArr=words.split(" ").sort(function(a,b){
      return a.match(/\d/)-b.match(/\d/)
    })
    //we can use any type condition along with regex inside our compare function to determine the order in which our data should be sorted
    return stringArr.join(" ")
  }