# Day 1: Mean, Median, Mode
import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))

# Day 0: Weighted Mean
n = int(input())
nums = [int(x) for x in input().split()]
weight = [int(x) for x in input().split()]

weighted_mean = sum([nums[i]*weight[i] for i in range(n)])/ sum(weight)
print(round(weighted_mean, 1))

# Day 1: Quartiles
from statistics import median
n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
t=int(len(arr)/2)
if len(arr)%2==0:
    L=arr[:t]
    U=arr[t:]
else:
    L=arr[:t]
    U=arr[t+1:]
    
print(int(median(L)))
print(int(median(arr)))
print(int(median(U)))

# Day 1:  Standard Deviation
n = int(input())

arr = [int(i) for i in input().split()]

mu = sum(arr) / n

difference_arr = [(arr[i]-mu)**2 for i in range(n)]

std_dev = (sum(difference_arr) / n)**.5

print ("{:.1f}".format(std_dev))

# Day 1: Interquartile Range
from statistics import median
n=int(input())
nums=[int(x) for x in input().split()]
freq =[int(x) for x in input().split()]

arr=[]
i = 0
for rep in freq: 
    for x in range(rep): 
        arr.append(nums[i])
    i +=1

arr.sort()
t=int(len(arr)/2)
if len(arr)%2==0:
    L=arr[:t]
    U=arr[t:]
else:
    L=arr[:t]
    U=arr[t+1:]

iqr = median(U)-median(L)

print("{:.1f}".format(iqr))