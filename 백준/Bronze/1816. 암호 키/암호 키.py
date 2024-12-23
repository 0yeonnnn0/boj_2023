def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        if (is_prime[p] == True):
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    prime_list = [p for p in range(2, max_num + 1) if is_prime[p]]
    return prime_list

N = int(input())
primes = sieve_of_eratosthenes(1000000)

for _ in range(N):
    S = int(input())
    is_valid = True
    for prime in primes:
        if S % prime == 0:
            is_valid = False
            break
    if is_valid:
        print('YES')
    else:
        print('NO')