function vowel2index(str) {
    var pattern = /[aeiouAEIOU]/
    var return_str = ""
     for(let i = 0;i < str.length ; i++){
       if(pattern.test(str[i])){
         return_str += i+1
       }else{
         return_str += str[i]
       }
     }
    return return_str
  }