def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = []
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
    return primes

primes = sieve_of_eratosthenes(1000000)

N = int(input())
for _ in range(N):
    S = int(input())
    is_valid_key = True
    for prime in primes:
        if S % prime == 0:
            is_valid_key = False
            break
    if is_valid_key:
        print('YES')
    else:
        print('NO')