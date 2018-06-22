xf = 0
yf = 0
zf = 0

i = 0
while (3 * i) < 1000:
    xf = xf + (3 * i)
    i = i + 1

j = 0
while (5 * j) < 1000:
    yf = yf + (5 * j)
    j = j + 1

k = 0
while (15 * k) < 1000:
    zf = zf + (15 * k)
    k = k + 1

print(xf+yf-zf)
# Finished
