# Check number bigger than 20
Number = 21
Divider = 20
passed = 0
while not passed:
    i = 2
    Number = Number + 1
    while ((Number % i) == 0) and (i <= Divider):
        if (Number % i) == 0:
            i = i + 1
        if i == Divider:
            if (Number % Divider) == 0:
                passed = 1

print(Number)
# Finished
