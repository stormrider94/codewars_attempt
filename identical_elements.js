function duplicateElements(m, n) {
    return m.some((v,i,arrayM)=>arrayM.includes(n[i]))
  }
  //    v represents the value of the current element being processed
  // i represents the index of the current element being processed
  // arrayM represents the array "m" on which .some is being called upon
  // arrayM.includes will determine whether arrayM has any ith element of n(i.e any element in n) 