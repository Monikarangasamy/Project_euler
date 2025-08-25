# Problem number 1
# Multiples of 3 or 5

def Multiples():
    output=0
    for i in range(1,1000):
        if i%3 ==0 or i%5==0:
            output+=i
    return output
print(Multiples())


#method 2 with O(1) time complexity

def sum_of_multiples_optimized():
    value=1000
    def sum(k):
        n = (value - 1) // k
        return k * n * (n + 1) // 2
    return sum(3) + sum(5) - sum(15)

print(sum_of_multiples_optimized())



