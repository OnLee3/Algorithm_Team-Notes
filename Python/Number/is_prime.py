# eratos

n = int(input())
is_prime = [True]*(n+1)


def eratos(n):
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False


eratos(n)
for i in range(2, n+1):
    if is_prime[i]:
        print(i, end=' ')

# 소수인 배열 자체를 리턴


def eratos(n):
    is_prime = [True] * (n+1)
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                if is_prime[j]:
                    is_prime[j] = False
    return [2] + [i for i in range(3, n+1, 2) if is_prime[i]]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
