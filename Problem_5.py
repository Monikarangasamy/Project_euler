def smallest_multiple():
    num = 20
    while True:
        for i in range(1, 21):
            if num % i != 0:
                break
        else:
            return num
        num += 1

print(smallest_multiple())
