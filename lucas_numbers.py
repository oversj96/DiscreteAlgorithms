# Lucas Numbers

def lucas_numbers(n):
    numbers = [2, 1]
    i = 2
    while(len(numbers)-1 < n):
        numbers.append(numbers[i-1] + numbers[i - 2])
        i += 1
    return numbers


print (lucas_numbers(20))

# [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2207, 3571, 5778, 9349, 15127]