function sieve(n) {
    let prime = new Array(n + 1).fill(true);
    // for (let p = 2; p * p <= n; p++) 
    let p = 2;
    while ((p*p) <= n)
    {
        if (prime[p]) {
          
            for (let i = p * p; i <= n; i += p) {
                prime[i] = false;
            }
        }
        p++;
    }
    let total = 0;
    for (let p = 2; p <= n; p++) {
        if (prime[p]) {
            total += p;
        }
    }

    return total;
}

console.log(sieve(2000000))
