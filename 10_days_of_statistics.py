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

import math

# equation l^k * e^-l / k!

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

l = float(input())
k = float(input())

prob = ((l**k)*math.exp(-l))/fact(k)

print(round(prob, 3))


# Day 5 Poisson distribution II

a, b = [float(num) for num in input().split(" ")]

ans_a = 160+40*(a + a**2)

ans_b = 128 + 40*(b + b**2)

print(round(ans_a, 3))

print(round(ans_b, 3))

# Day 5 Normal Distribution 

import math
mean, std = 20, 2
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
print('{:.3f}'.format(cdf(19.5)))
# Between 20 and 22
print('{:.3f}'.format(cdf(22) - cdf(20)))

# Day 5 Normal Distribution II

import math
mean, std = 70, 10
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

#grade >80
print('{:.2f}'.format((1 - cdf(80))* 100))
#grade >=60
print('{:.2f}'.format((1- cdf(60))* 100))
#grade <60
print('{:.2f}'.format(cdf(60)*100))

# Day 6 Central Limit Theroem

import math

# Elavator capacity = 9800 lbs
# Number of boxes = 49
# Average weight of boxes = 205
# Std of boxes = 15

# Question:  What is the probability that all the boxes weigh less than 9800 lbs

x = float(input())
n = float(input())
mean = float(input())
std = float(input())

#Because clt

mean_prime = n * mean
std_prime = math.sqrt(n) * std

cdf = lambda x: 0.5 * (1 + math.erf((x - mean_prime) / (std_prime * (2 ** 0.5))))

print(round(cdf(9800), 4))
