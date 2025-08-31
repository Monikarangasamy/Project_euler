# def digit_fact():
#     n = int(input("enter the value "))
#     sum = 0
#     original = n
#     while n != 0:
#         digit = n % 10
#         fact = 1
#         for i in range(1, digit+1):
#             fact = fact * i
#         sum += fact
#         n = n // 10
#     if sum == original:
#         return sum
#     else:
#         return -1
            
# print(digit_fact())



digit_factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
def is_curious(n):
    s = 0
    for d in str(n):      
        s += digit_factorials[int(d)]   
    return s == n

total = 0
for num in range(10, 1000000):   
    if is_curious(num):
        total += num

print(total)

