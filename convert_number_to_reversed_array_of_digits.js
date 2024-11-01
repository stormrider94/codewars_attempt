function digitize(n) {
    let array1 = Array.from(n.toString())
    console.log(array1)
    let array2 = array1.map((item)=> Number(item))
    
    console.log(array2)
    let reversedArray = array2.reverse()
    return reversedArray
    //code here
  }