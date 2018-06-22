from array import array

# Declare List and index numbers
PrimeNumber = 10001
Primes = [2, 3, 5, 7]
number = 8
divider = 0
check = 0

# While length of array is <= 10001, find primes
while len(Primes) <= PrimeNumber:
    divider = 2
    check = 0
# Divide number by values greater than one but less than number
    while (check == 0) and (divider < number):
        if (number % divider) == 0:  # Value cannot be prime.
            check = 1  # Flagged as not prime.
        divider = divider + 1
    # If the result has a remainder for every case, it's prime.
    if check == 0: # If the number is prime, add to an array.
        Primes.append(number)
    number = number + 1

print(Primes[PrimeNumber - 1])
# Finished
