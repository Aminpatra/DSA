# https://codeforces.com/contest/460/problem/A

# Topic: implementation/math
# Rating: A: 900

# Time took to solve problem is: 10 mins.
# Solved in Fifth try.
# AI used ? yes (small hint for + n % m part only)

n, m=map(int,input().split())
tot=n
while (n//m):
  tot += n//m
  n = n //m + n % m
print(tot)