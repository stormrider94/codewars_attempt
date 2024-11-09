function powerSumDigTerm(n) {
    const series = [0]
      for(let i = 2; i<99; i++){
        for(let j=2; j<42; j++){
          let  k = i**j
          let accumulator = 0
          //if we sum all the digits in the power and it is equal to the base digit
          //eg. k = 81, i= 9, j= 2 if (8+1 === i which is 9) push it to the array containing those unique value
          k.toString().split("").forEach((x)=>{
            accumulator += parseInt(x)
          })
          if(i === accumulator){
            series.push(k)
          }
        }
      }
    const sum_digits_sorted = series.sort(function(a,b){
      return a-b
    })
    console.log(sum_digits_sorted)
    console.log(sum_digits_sorted[n])
    return sum_digits_sorted[n]
  }