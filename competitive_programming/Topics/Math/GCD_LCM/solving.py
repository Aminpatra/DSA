# from functools import reduce
from math import gcd

n = int(input())
nums = list(map(int,input().split()))
g = nums[0]
for i in range(1, n):
  g = gcd(g, nums[i])

count = 0

i = 1

while i * i <= g:
  if (g % i == 0):
    count += 1
    if (g // i != i):
      count += 1
  i += 1

print(count)