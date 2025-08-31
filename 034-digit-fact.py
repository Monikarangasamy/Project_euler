def digit_fact():
    n = int(input("enter the value "))
    sum = 0
    original = n
    while n != 0:
        digit = n % 10
        fact = 1
        for i in range(1, digit+1):
            fact = fact * i
        sum += fact
        n = n // 10
    if sum == original:
        return sum
    else:
        return -1
            
print(digit_fact())