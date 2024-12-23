MAX_PRIME = 1000000
is_prime = [True] * (MAX_PRIME + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX_PRIME**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_PRIME + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, MAX_PRIME + 1) if is_prime[i]]

N = int(input())
for _ in range(N):
    S = int(input())
    is_valid_key = True
    for prime in primes:
        if prime * prime > S:
            break
        if S % prime == 0:
            is_valid_key = False
            break
    if is_valid_key:
        print('YES')
    else:
        print('NO')