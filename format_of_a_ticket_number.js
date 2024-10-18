function nbrValidTickets(tickets){
 const pattern = /^[a-zA-Z][0-9][a-zA-Z]{4}$/
 let count = 0;
  for (const ticket of tickets){
    if(pattern.test(ticket)){
      count ++
    }
    
  }
  return count
}