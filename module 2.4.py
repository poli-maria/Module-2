numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is_prime = []
not_prime = []
for num in numbers:
    if num == 1:
        continue
    else:
        prime = True
        for i in range(2, num//2+1):
            if num % i == 0:
                prime = False
                break
        if prime:
            is_prime.append(num)
        else:
            not_prime.append(num)
print(f'Primes: {is_prime}')
print(f'Not Primes: {not_prime}')