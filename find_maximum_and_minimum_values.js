var min = function(list){
    let arrangedlist=list.sort(function(a,b){
      return a-b
    })
  //   we need to sort the list in ascending order
      return arrangedlist[0];
  }
  
  var max = function(list){
    let arrangedlist=list.sort(function(a,b){
      return a-b
    })
    let rearrangedList = arrangedlist.reverse()
      //we reverse the sorted list 
      return rearrangedList[0];
  }