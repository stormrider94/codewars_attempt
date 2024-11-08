function insertDash(num) {
    const num_arr = num.toString().split("")
     let return_str = ""
     for (let i = 0 ; i < num_arr.length; i++){
       const curr = num_arr[i]
       const next = num_arr[i+1]
       if(Number(curr)%2 == 1 && Number(next)%2 == 1){
         return_str += curr
         return_str += "-"
       }
       else {
         return_str += curr
       }
     }
     return return_str
   }