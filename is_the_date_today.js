function isToday(date) {
  //get today's date
  const date_today = new Date().toISOString().split(".")[0].split("T")[0]
  const date_param = date.toISOString().split(".")[0].split("T")[0]
  console.log(date_today)
  console.log(date_param)
  //compare it to the date string passed as a parameter
  return date_today == date_param
}