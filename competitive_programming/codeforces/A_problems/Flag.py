# http://codeforces.com/contest/16/problem/A
# Topic: implementation
# Rating: A - 800 

# Time took to solve problem is: 7 min.
# Solved in Third try.
# AI used ? NO


n,m=map(int,input().split())
t_colors = set()
prev = input()
f=True
if (len({*prev}) != 1): f=False
else:
  t_colors.add(prev[0])
  
  for i in range(n-1):
    row = input()
    if (len({*row}) != 1) or (row == prev): f = False
    else: prev = row

if len(t_colors) != 10 and f: print("YES")
else: print("NO")