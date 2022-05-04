rev_base = ''
while n > 0:
    n, mod = divmod(n, k)
    rev_base += str(mod)

print(rev_base[::-1])
