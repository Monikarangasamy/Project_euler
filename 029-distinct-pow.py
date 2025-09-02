def distinct_powers(n):
    distinct_terms = set()
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            distinct_terms.add(a ** b)
    return len(distinct_terms)

print(distinct_powers(100))  