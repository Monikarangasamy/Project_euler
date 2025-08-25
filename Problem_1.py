# Problem number 1
# Multiples of 3 or 5

def Multiples():
    output=0
    for i in range(1,1000):
        if i%3 ==0 or i%5==0:
            output+=i
    return output
print(Multiples())

