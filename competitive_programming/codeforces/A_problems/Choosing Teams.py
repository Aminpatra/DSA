# http://codeforces.com/contest/432/problem/A
# Topic: greedy
# Rating: A: 800

# Time took to solve problem is: 7 min.
# Solved in First try.
# AI used ? NO

n, k=map(int,input().split())
teams = 0
members = sorted(list(map(int,input().split())))
if n < 3: print(0)
else: 
  for i in range(2, n, 3):
    if members[i] + k <= 5: teams += 1
  print(teams)
