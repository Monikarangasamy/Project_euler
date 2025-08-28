def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_prime(limit):
    total = 0
    for num in range(2, limit):
        if is_prime(num):
            total += num
    return total

print(sum_of_prime(2000000))


