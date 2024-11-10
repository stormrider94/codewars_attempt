function findUniq(arr) {
    // do magic
    let filtered = arr.map((s)=>{
      l = s.toLowerCase();
      l  = l.replace(/\s+/gi, "");
      l=new Set(l)
      l=[...l].sort().join("")
      return l;
  });
    
  let obj={};
    for(let i = 0; i < filtered.length; i++){
      if(obj[filtered[i]] === undefined){
          let ar = [];
          obj[filtered[i]] = ar;
          obj[filtered[i]].push(i);
      }
      else{
          obj[filtered[i]].push(i)
      }
  }
  let experimentalarray=Object.keys(obj)
    for(let i=0;i<experimentalarray.length;i++){
      if(obj[experimentalarray[i]].length===1){
      //the unique element has only one index,therefore returing ...[0] gives us the only element
         return arr[obj[experimentalarray[i]][0]];
      }
  }
  }