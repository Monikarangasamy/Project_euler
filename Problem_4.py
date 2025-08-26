#problem number 4
#Largest palindrome product number

def palindrome():
    max_palindrome = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            product = i * j
            temp = product
            result = ""
            while temp != 0: #reverse a interger
                digit = temp % 10
                temp = temp // 10
                result += str(digit)
            if str(product) == result: # check palindrome
                if product > max_palindrome:
                    max_palindrome = product
    return max_palindrome

print(palindrome())

#method 2 

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

