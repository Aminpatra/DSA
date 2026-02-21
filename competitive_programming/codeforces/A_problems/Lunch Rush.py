# http://codeforces.com/contest/276/problem/A
# Topic: implementation
# Rating: A - 900 

# Time took to solve problem is: 10 min.
# Solved in Second try.
# AI used ? NO

n, k = map(int,input().split())
mx = float('-inf')
for _ in range(n):
  f, t= map(int, input().split())
  if t > k: mx = max(mx, (f-(t-k)))
  else: mx = max(mx, f)
print(mx)