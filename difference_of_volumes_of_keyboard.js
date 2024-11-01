function findDifference(a, b) {
    let firstProduct=a.reduce((previousValue,currentValue)=>previousValue*currentValue,1)
    let secondProduct=b.reduce((previousValue,currentValue)=>previousValue*currentValue,1)
    let value=firstProduct>secondProduct?firstProduct-secondProduct:secondProduct-firstProduct
    return value
    
  }