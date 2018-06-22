StartVal = 600851475143
Divider = 2
LargePrime = 0
i = 0

while (Divider > 0) and (LargePrime == 0):
    if (StartVal % Divider) == 0:
        i = 2
        while ((Divider % i) != 0) and (i < Divider) and (LargePrime == 0):
            if Divider == i + 1:
                LargePrime = Divider
            i = i + 1
    Divider = Divider - 1
    print(Divider)

print("Solution:")
print(LargePrime)
