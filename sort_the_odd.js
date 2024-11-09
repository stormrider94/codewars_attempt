function sortArray(array) {
    odd_arr = array.filter((elem)=>elem % 2)
    sorted_odd = odd_arr.sort(function(a,b){
      return a-b
    })
    console.log(sorted_odd)
    result = array.map((elem)=>{
      if(elem%2) return sorted_odd.shift()
      else return elem
    })
    console.log(result)
  return result
  }