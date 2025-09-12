function isLeapYear(year) {
  if (year % 400 === 0) return true;
  if (year % 100 === 0) return false;
  if (year % 4 === 0) return true;
  return false;
}

const daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

let dayOfWeek = 2; 
let count = 0;

for (let year = 1901; year <= 2000; year++) {
  for (let month = 0; month < 12; month++) {
    if (dayOfWeek === 0) {
      count++;
    }

    let days = daysInMonth[month];
    if (month === 1 && isLeapYear(year)) {
      days = 29;
    }

    dayOfWeek = (dayOfWeek + days) % 7;
  }
}

console.log(count);
