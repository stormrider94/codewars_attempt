function getCount(str) {
    var vowelsCount = 0;
    let StringArray=Array.from(str)
    StringArray.forEach(element=>{
      if(element==='a'||element==='e'||element==='i'||element==='o'||element==='u'){
        vowelsCount++
  }
    })
    
    
    return vowelsCount;
  }