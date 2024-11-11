function orderFood(list) {
    let foodcount={}
    list.forEach((dev)=>{
      if(dev.meal in foodcount)foodcount[dev.meal]++
      else foodcount[dev.meal]=1
    })
    console.log(foodcount)
    return foodcount
  }