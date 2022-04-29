import random
n = 4
m = 4
From = 0
To = 7

# 랜덤 정수
print(random.randrange(From, To))

# 랜덤 배열
for i in range(n):
    for j in range(m):
        print(random.randrange(From, To), end=' ')
    print()

# 랜덤 알파벳
for i in range(n):
    for j in range(m):
        print(chr(random.randrange(65, 90)), end=' ')  # 소문자 97 - 122
    print()
