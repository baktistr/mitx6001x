def rec(n):
    if n == 1:
        return 1
    else:
        return n* rec(n-1)

n=3
print (rec(n))
