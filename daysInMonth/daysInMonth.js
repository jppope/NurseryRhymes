/*
 Thirty days hath September,
 April, June, and November;
 All the rest have thirty-one,
 Excepting February alone,
 Which has twenty-eight in line,
 Till leap-year gives it twenty-nine.
 */


// As an Array (super simple)
var numDaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

// written as just an object (super simple)
var daysInMonth = {
 "28": "February",
 "30": ["September", "April", "June", "November"],
 "31": ["January", "March", "May", "July", "August", "October", "December"]
}
//basic if/else function to determine how many days are in a month

function howManyDaysInMonth(month) {
 //standardize the input
 month = month.toLowerCase();
 if (month == "september" || month == "april" || month == "june" || month == "november") {
  //console.log(30);
  return 30;
 } else if (month === "february") {
  return 28;
 } else {
  return 31;
 }
}
console.log(howManyDaysInMonth("october"));