// function isPrime(num) {
//   if (num <= 1) return false;
//   if (num <= 3) return true;
//   if (num % 2 === 0 || num % 3 === 0) return false;

//   for (let i = 5; i * i <= num; i += 6) {
//     if (num % i === 0 || num % (i + 2) === 0) {
//       return false;
//     }
//   }
//   return true;
// }
// function findNthPrime(n) {
//   if (n === 1) return 2;
  
//   let count = 1;
//   let candidate = 1;

//   while (count < n) {
//     candidate += 2;
//     if (isPrime(candidate)) {
//       count++;
//     }
//   }
//   return candidate;
// }

// const target = 10001;
// console.log(`The ${target}st prime number is: ${findNthPrime(target)}`);

function findNthPrime(n) {
  const limit = 120000;
  const isPrime = new Array(limit).fill(true);

  isPrime[0] = false;
  isPrime[1] = false;

  let count = 0;

  for (let p = 2; p < limit; p++) {
    if (isPrime[p] === true) {
      count++;

      if (count === n) {
        return p;
      }
      for (let i = p * p; i < limit; i += p) {
        isPrime[i] = false;
      }
    }
  }

  return -1;
}
const target = 10001;
const result = findNthPrime(target);

console.log(`The ${target}st prime number is: ${result}`);