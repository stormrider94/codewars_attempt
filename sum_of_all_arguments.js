function sum(...numbers) {
    // return the sum of all arguments given.
    let sum = 0
    for (const num of numbers){
      sum += num
    }
    return sum
  }