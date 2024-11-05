function isAlphanumeric(char) {
    // Regular expression to match alphanumeric characters
    var alphanumericRegex = /^[0-9a-zA-Z]+$/;
    return alphanumericRegex.test(char);
}
function isNumber(value) {
    return !isNaN(value);
}
function isLetter(character) {
    return /^[a-zA-Z]+$/.test(character);
}

function validPass(password){
  // if there is one character and there is one number we set a variable to signify that 
  //it has passed the requirments
  let contains_alphanumeric_only = true
  let contains_at_least_one_letter = false
  let contains_at_least_one_number = false
  len = password.length
  let within_number_of_chars = (len >3 && len < 20)
  for(let i=0; i<len; i++){
    if(!isAlphanumeric(password[i])){
    contains_alphanumeric_only = false    
    }
    else if(isNumber(password[i])){
      contains_at_least_one_number = true
      console.log("there is a number here")
    }
    else if(isLetter(password[i])){
      contains_at_least_one_letter = true
      console.log("there is a letter here")
    }
  }
  if (contains_alphanumeric_only && contains_at_least_one_letter && contains_at_least_one_number && within_number_of_chars){
    return "VALID"
  }
  else {
    return "INVALID"
  }
}