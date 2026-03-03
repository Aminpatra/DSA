# https://codeforces.com/contest/272/problem/A
# Topic: implementation/math
# Rating: A: 1000

# Time took to solve problem is: 8 min.
# Solved in First try.
# AI used ? NO

n=int(input())
fingers = sum(map(int,input().split()))
ways=0
for i in range(1, 6):
  if (((fingers + i) % (n+1)) != 1): 
    ways += 1
print(ways)
