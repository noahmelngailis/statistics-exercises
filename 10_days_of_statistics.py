# Day 4 Binomial Distribution

def fact(n):
    return 1 if n==0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

l, r = list(map(float, input().split(" ")))
odds = l / r

print(round(sum([b(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3))


# Day 4 Binomial Distributions 2

def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

p, n = list(map(int, input().split(" ")))
print(round(sum([b(i, n, p/100) for i in range(3)]), 3))
print(round(sum([b(i, n, p/100) for i in range(2, n+1)]), 3))

# Day 4 Geometric Distributution
num, den = list(map(int, input().split(" ")))
n = int(input())

p = num/den

print(round((1-p)**(n-1)*p, 3))

# Day 4 Geometric Distribution II
num, dem = list(map(int, input().split(" ")))
n = int(input())

p = num / dem

print(round((1-(1-p)**n), 3))

# Day 5 Poisson distribution

# Here is where the poisson distribution answer will go