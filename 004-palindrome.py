#problem number 4
#Largest palindrome product number

def ispalindrome(n):
    original = str(n)
    reverse = original[::-1]
    return original == reverse

def palindrome():
    max_palindrome = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            product = i * j
            if product > max_palindrome and ispalindrome(product):
                    max_palindrome = product
    return max_palindrome

print(palindrome())
