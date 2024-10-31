function getMiddle(s)
{var middle
 let stringArr = s.split("")
 console.log(stringArr)
 if(stringArr.length % 2== 1){
   middle = stringArr[Math.floor((stringArr.length)/2)]
 }else{
   middle = stringArr[Math.floor((stringArr.length + 1)/2)-1] + stringArr[Math.ceil((stringArr.length + 1)/2)-1]
  }
 console.log(middle)
 return middle
}