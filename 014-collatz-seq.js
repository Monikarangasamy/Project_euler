function collatz(limit) {
  const memo = {1: 1}; 
  let maxLen = 0;
  let startingNum = 1;

  for (let n = 1; n <= limit; n++) {
    let i = n;
    let steps = 0;

    while (!memo[i]) {   
      if (i % 2 === 0) {
        i = i / 2;
      } else {
        i = 3 * i + 1;
      }
      steps++;
    }

    memo[n] = steps + memo[i];  

    if (memo[n] > maxLen) {   
      maxLen = memo[n];
      startingNum = n;
    }
  }

  return startingNum
}
console.log(collatz(1000000));