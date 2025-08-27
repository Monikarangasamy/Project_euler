# def smallest_multiple():
#     num = 20
#     while True:
#         for i in range(1, 21):
#             if num % i != 0:
#                 break
#         else:
#             return num
#         num += 1

# print(smallest_multiple())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_result(n):
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result

print(lcm_result(20))