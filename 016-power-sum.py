#problem number 16
#power digit sum

def power_sum():
    n = 2**1000
    sum = 0
    while (n != 0):
        digit = n % 10
        sum += digit
        n = n // 10
        
    return sum
print(power_sum())

