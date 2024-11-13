function divisors(integer) {
    //we create an empty array to store the divisors 
   let DivisorArray=[]
   //we divide the integer by all the numbers between 2 and the number exclusive
   //hence the number of times the loop will run isn't specific but dependent on the integer
   for(let i=2;i<integer;i++){
     let remainder=integer%i
     //divisors are integers which can easily divide a number leaving no remainder 
     if(remainder===0){
      // we add the number to the array we want to return 
       DivisorArray.push(i)}
     }
    /*The code below is outside the loop so what this means is that after the loop has 
    finished executing,if the DIVISORARRAY  is empty,this means no number 
    can divide the number except for 1 and the number itself hence 
    the number is prime*/
   if(DivisorArray.length==0)
   {return integer + " is prime"}                          
   else{return DivisorArray}
 };