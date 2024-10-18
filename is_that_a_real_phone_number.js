function validateNumber(str){
  const phone_number = str.replace(/[^0-9+]/g,"") //this even removes the dashes ("-")
  if(!phone_number){
    return "Plenty more fish in the sea"
  }
  // regular expression for valid formats
  const regex = /^(?:\+44)?(?:0)?7\d{9}$/
  return regex.test(phone_number)?"In with a chance" : "Plenty more fish in the sea"
}