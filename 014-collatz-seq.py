def collatz_seq():
    max_val = 0
    starting_num = 0
    for n in range(1, 1000001):   
        i = n
        count = 0
        while i > 1:
            if i % 2 == 0:
                i = i // 2
            else:
                i = 3*i + 1
            count += 1
        if count > max_val:
            max_val = count
            starting_num = n  
    return starting_num

print(collatz_seq())