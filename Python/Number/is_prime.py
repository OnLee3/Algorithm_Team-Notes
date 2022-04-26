# eratos
import math

n = int(input())
is_prime = [True]*(n+1)


def eratos(n):
    for i in range(2, int(math.sqrt(n))+1):
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
    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                if is_prime[j]:
                    is_prime[j] = False
    return [2] + [i for i in range(3, n+1, 2) if is_prime[i]]
