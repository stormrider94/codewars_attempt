const passwords_signed_in = []
var signIn = function(newPassword) {
  passwords_signed_in.push(newPassword)
};
var logIn = function(password) {
  return passwords_signed_in.includes(password)
};