prime_ends = [1, 3, 7, 9]
primes = [2, 3, 5, 7, 9]
max = 9
number = 10

while len(primes) < 100000:  # Determine the first 100,000 primes.
    if number % 10 in prime_ends:
        for y in primes:
            if number % y is 0:
                break
            elif y is max and number % y is not 0:
                primes.append(number)
                max = number
                break
    number += 1
with open("primes.txt", "w") as txt:
    for prime in range(0, len(primes)):
        txt.write(f"P = {prime+1} : {primes[prime]}\n")
