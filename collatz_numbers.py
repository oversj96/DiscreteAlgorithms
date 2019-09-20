# Collatz Numbers

def collatz_numbers(n):
    numbers = [n]
    i = 0
    while(numbers[i] is not 1):
        if(numbers[i] % 2 == 0):
            numbers.append(numbers[i]//2)
        else:
            numbers.append(3 * numbers[i] + 1)
        i += 1
    return len(numbers), numbers


print (collatz_numbers(108))

# [39, 118, 59, 178, 89, 268, 134, 67, 202, 101, 304, 152, 76, 38, 19, 58, 29, 88, 
# 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]