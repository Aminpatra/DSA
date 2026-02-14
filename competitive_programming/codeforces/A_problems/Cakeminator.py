# http://codeforces.com/contest/330/problem/A
# Topic: implementation
# Rating: A: 800

# Time took to solve problem is: 15 min.
# Solved in Second try.
# AI used ? NO

n,m=map(int,input().split())
grid = []
entire_rows = 0
t = 0
for i in range(n):
  row = input()
  if 'S' not in row: 
    entire_rows += 1
    t += m
  grid.append(row)

for i in range(m):
  found_s = False
  for j in range(n):
    if grid[j][i] == 'S':
      found_s = True
      break
  if not found_s:
    t += (n - entire_rows)
print(t)