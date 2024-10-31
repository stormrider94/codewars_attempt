function descendingOrder(n){
    //   we first convert the input to string
        let passedNumber=String(n);
      //we split the string into an array using Array.from
        let stringsArray=Array.from(passedNumber);
    //   we sort the array in descending order using the sort along with the compare function
        let sortedArray=stringsArray.sort(function(a,b){return b-a});
        let finalAnswer="";
    
        for(let i=0;i<sortedArray.length;i++){
          //we concatenate the string from the loop
            finalAnswer+=sortedArray[i];
        }
    //   we then convert the string into a number
        let finalValue=Number(finalAnswer);
        return finalValue
    }