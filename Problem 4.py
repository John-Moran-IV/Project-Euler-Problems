import numpy as np

Solved = 0
x = 999
y = 999
Product = 0
Palindromes = []

# Outer loop for first multiplier, start at 999 and go down.
while x > 0:
    Product = x * y
    Rev = 0
    n = Product
    while n > 0:
        Dig = n % 10
        Rev = Rev * 10 + Dig
        n = n // 10
    if Product == Rev:
        Palindromes.append(Product)

    while y > 0:
        Product = x * y
        Rev = 0
        n = Product
        while n > 0:
            Dig = n % 10
            Rev = Rev * 10 + Dig
            n = n // 10
        if Product == Rev:
            Palindromes.append(Product)
        y = y - 1
    y = 999
    x = x - 1

MaxPali = np.amax(Palindromes)
# Inner loop for second multiplier, start at 999 and go down.

# Categorize product into odd and even number of digits.

# Use formula to check if number is a palindrome

# If either category shows a palindrome, Solved = true.

print(MaxPali)
# Finished
