# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def sum_of_prime(limit):
#     total = 0
#     for num in range(2, limit):
#         if is_prime(num):
#             total += num
#     return total

# print(sum_of_prime(2000000))

def sieve(n):
  
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    total=0
    for p in range(2, n + 1):
        if prime[p]:
           total += p
    
    return total
print(sieve(2000000))
