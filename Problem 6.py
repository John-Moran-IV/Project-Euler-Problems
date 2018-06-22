i = 0
j = 0
sumSq = 0
sqSum = 0
jSum = 0
Diff = 0

for i in range(1,101,1):
    sumSq = sumSq + i ** 2
print(sumSq)

for j in range(1,101,1):
    jSum = jSum + j

sqSum = jSum ** 2
print(sqSum)

Diff = sqSum - sumSq
print(Diff)
# Finished
