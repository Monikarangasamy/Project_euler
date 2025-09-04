def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 2  
        i += 1
    if int(n**0.5) ** 2 == n:  
        count -= 1
    return count

def triangle_with_divisors(limit):
    n = 1
    triangle = 1
    while True:
        divs = count_divisors(triangle)
        if divs > limit:
            return triangle
        n += 1
        triangle += n

print(triangle_with_divisors(500))


