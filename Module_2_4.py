numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
is_prime = True
for i in range(len(numbers)):
    for j in range(2,numbers[i]):
        if (numbers[i] % j==0):
            is_prime = False
            not_prime.append(numbers[i])
            break
        else:
            is_prime = True
    if (is_prime):
        prime.append(numbers[i])
print(prime)
print(not_prime)