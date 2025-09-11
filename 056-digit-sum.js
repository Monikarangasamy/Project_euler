function digitSum(n) {
  let sum = 0;
  for (const ch of n.toString()) { 
    sum += Number(ch);               
  }
  return sum;
}

function maxDigitSum() {
  let maxVal = 0;

  for (let a = 50; a < 100; a++) {
    for (let b = 50; b < 100; b++) {
      let result = BigInt(a) ** BigInt(b); 
      let sum = digitSum(result);          
      if (sum > maxVal) {
        maxVal = sum;
      }
    }
  }
  return maxVal;
}

console.log(maxDigitSum()); 
