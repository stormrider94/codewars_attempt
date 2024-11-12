function solve(s){
    //first I have to get access to all the substrings in the passed string and push them into an empty array
    let oddNumberArray = [] 
    const BigNumber = require('bignumber.js')
    //in rder to enhance arithmetic precision so that all random numbers work,
  //   we have to use an API for mathematical precision
    for(i=0; i<s.length;i++){
      for(j=i+1 ;j<s.length+1 ;j++ ){
        let y =new BigNumber((s.slice(i,j)))
  //       precision is important for things like decimals,negative numbers,0 and stuff
        if(y.modulo(2)*1===1) oddNumberArray.push(y)
        }
      }
    return oddNumberArray.length
    
  };