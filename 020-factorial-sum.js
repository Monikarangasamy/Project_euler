function factorialSum(n){
  let fact = 1n;
  for (i = 2n; i <= n; i++){
    fact *= i;
    }

    let num = fact.toString();
    let sum = 0;
    for (let digit of num){
      sum += Number(digit);
    }
    return sum;
}
console.log(factorialSum(100))


