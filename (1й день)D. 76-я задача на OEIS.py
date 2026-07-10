def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
 
 
def get_primes(count):
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
 
 
t = int(input())
for _ in range(t):
    n = int(input())
 
    primes = get_primes(n - 1)
 
    a = [1]
 
    a.append(primes[0])
 
    for i in range(1, n - 1):
        a.append(primes[i - 1] * primes[i])
 
    print(' '.join(map(str, a)))
