function findSenior(list) {
  // thank you for checking out the Coding Meetup kata :)
  let oldestAge=list[0].age
  list.forEach(dev=>{
    if(dev.age>oldestAge) oldestAge=dev.age
  })
  console.log(list.filter(dev=>dev.age===oldestAge))
  return list.filter(dev=>dev.age===oldestAge)
  
}