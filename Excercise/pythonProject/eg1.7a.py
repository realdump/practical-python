def sumcount(n):
    total = 0
    while n > 0:
        total+=n
        n-=1
    return total

a = sumcount(10)

print(a)
