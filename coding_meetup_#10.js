function addUsername(list) {
    let today=new Date()
  console.log(today.getFullYear())
    let currentYear=today.getFullYear()
   let newList=list.map((developer)=>{
      let BirthYear=currentYear-developer.age
      let newfirstName=developer.firstName.toLocaleLowerCase()
      let regex=/[.]/
      let newLastName=developer.lastName.toLocaleLowerCase()
      newLastName=newLastName.replace(regex,"")
      developer.username=`${newfirstName}${newLastName}${BirthYear}`
      return developer
  })
   console.log(newList)
   return newList
  }