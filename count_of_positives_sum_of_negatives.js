function countPositivesSumNegatives(input) {
    let sumNegative=0
    let outputArray=[]
    let counter=0
    if(input){
    if(input.length===0||input===""){
      return outputArray
      }
   input.forEach((element)=>{
   if(element>0){
     counter++
   }
     else if(element ===0){
       //do nothing
       }
      else{
       sumNegative=sumNegative+element
     }
     }
     
    )
    outputArray.push(counter)
     outputArray.push(sumNegative)
     return outputArray
      }
   else{
     return []
     }
 }