# https://codeforces.com/contest/447/problem/A

# Topic: implementation
# Rating: A: 800

# Time took to solve problem is: 3 mins.
# Solved in First try.
# AI used ? No

p, n=map(int, input().split())
visited=set()
f=False
ind = None
for i in range(1,n+1):
  num=int(input())
  if (num % p in visited):
    f=True
    if ind is None:
      ind = i
  else:
    visited.add(num % p)

print(ind if f else -1)