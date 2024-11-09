function isTwinPrime(n){
    //   check if number is prime
      function checkPrime(value){
        let factors=[]
        for(let i=1;i<=value;i++){
          if(value%i===0)factors.push(i)
        }
        console.log(factors)
        if(factors.length==2)return true
        else return false
      }
      console.log(checkPrime(9))
    //   a twin prime should be both a prime number and its difference of 2 should be a prime too 
      
    return checkPrime(n) &&(checkPrime(n+2)|| checkPrime(n-2))
    }