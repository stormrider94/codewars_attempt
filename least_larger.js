function leastLarger(a,i) {
    console.log(a)
    console.log(i)
    if(i>a.length) return -1
    let leastlargest=a.filter((number,index)=>{
      return number>a[i]})
    console.log(leastlargest)
    if(Math.min(...leastlargest)){
      //There are large numbers in the array ut we want the index of the least largest as the kata title says
      console.log(a.indexOf(Math.min(...leastlargest)))
      return a.indexOf(Math.min(...leastlargest))
      }
    else {
      console.log(-1)
      return -1
    }
    }
      