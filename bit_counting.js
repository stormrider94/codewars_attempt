var countBits = function(n) {
    const remainder_li = []
    let quotient = n
    let track_ones  = 0
    while(quotient != 0){
      const remainder = quotient % 2
      quotient = Math.floor(quotient / 2)
      if(remainder == 1){
        track_ones += 1
      }
      remainder_li.push(remainder)
    }
    console.log(remainder_li)
    return track_ones
  };