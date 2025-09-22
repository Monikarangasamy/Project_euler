ones = ["","one","two","three","four","five","six","seven","eight","nine",
        "ten","eleven","twelve","thirteen","fourteen","fifteen",
        "sixteen","seventeen","eighteen","nineteen"]
tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def num_to_words(n):
    if n < 20: return ones[n]
    if n < 100: return tens[n//10] + ("" if n%10 == 0 else "-" + ones[n%10])
    if n < 1000:
        return ones[n//100] + " hundred" + ("" if n%100 == 0 else " and " + num_to_words(n%100))
    if n == 1000: return "one thousand"

def letters_only(s):
    return len(s.replace(" ", "").replace("-", ""))
total = sum(letters_only(num_to_words(i)) for i in range(1, 1001))
print(total)




