function sc(floor){
    var scream = ""
    if(floor < 2){
      return ""
    }
    else if(floor > 6){
      for(let i = 0; i < floor; i++){
        if(i == floor-1){
          scream += "Pa!"
        }else{
          scream += "Aa~ "
        }
      }
    }else{
      for(let i = 0; i < floor + 1; i++){
        if(i == floor-1){
          scream += "Pa! "
        }else if(i== floor){
          scream += "Aa!"
        }else{
          scream += "Aa~ "
        }
      }
    }
    return scream.trim()
  }