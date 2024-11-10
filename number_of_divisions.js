const divisions = (n, divisor) => {
    let quotient=n
    let count=0
    while(quotient>=divisor){
      if(quotient/divisor){
        quotient=Math.floor(quotient/divisor)
        count++
      }
    }
    return count
  };