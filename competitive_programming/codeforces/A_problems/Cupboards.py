# https://codeforces.com/contest/248/problem/A
# Topic: implementation
# Rating: A: 800

# Time took to solve problem is: 5 min.
# Solved in First try.
# AI used ? NO

n = int(input())
l_zeros, r_zeros = 0, 0
for i in range(n):
  a,b=map(int,input().split())
  if a == 0: l_zeros += 1
  if b == 0: r_zeros += 1
print(min(n-l_zeros, l_zeros) + min(n-r_zeros, r_zeros))