function latticePaths(n) {
  let res = 1n;
  for (let k = 1n; k <= BigInt(n); k++) {
    res = res * (BigInt(n) + k) / k;
  }
  return res;
}

console.log(latticePaths(20).toString());
