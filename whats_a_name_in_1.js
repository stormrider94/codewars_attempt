function nameInStr(str, name){
    // let's convert str and name into lower cases 
     first_str = str.toLowerCase()
     name_str = name.toLowerCase()
     
     index = 0
     for(let i=0;i<first_str.length;i++){
       if(first_str[i]== name_str[index]){
         index ++
         if(index == name_str.length){
           return true
         }
       }
     }
     return false
   }