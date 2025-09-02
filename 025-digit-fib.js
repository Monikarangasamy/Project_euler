function digitFibonacci(n) {
  let a= 1n, b = 1n;
  let index = 2;
  while (b.toString().length < n) {
    [a, b] = [b, a + b];
    index++;
  }
    return index;
}
console.log(digitFibonacci(1000));

    