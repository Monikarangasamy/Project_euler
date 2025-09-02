function distinctPowers(limit) {
  const results = new Set();

  for (let a = 2; a <= limit; a++) {
    for (let b = 2; b <= limit; b++) {
      results.add(a ** b); 
    }
  }
  return results.size;
}

console.log(distinctPowers(100));
