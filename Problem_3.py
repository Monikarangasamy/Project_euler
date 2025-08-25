def large_prime():
    i = 2
    n=600851475143
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n

print(large_prime())