# http://codeforces.com/contest/275/problem/A
# Topic: implementation
# Rating: A - 900 

# Time took to solve problem is: 10 min.
# Solved in First try.
# AI used ? (This is the fourth time solving this problem, just wanted to know what is the best way to traverse the grid)

grid = []
for i in range(3):
  grid.append(list(map(int,input().split())))

for i in range(3):
  row = ''
  for j in range(3):
    total = grid[i][j]
    for di, dj in [(-1,0), (1, 0), (0, -1), (0, 1)]:
      ni, nj = i+di, j+dj
      if (0 <= ni < 3 and 0 <= nj < 3):
        total += grid[ni][nj]
    row += str((1+total) % 2)
  print(row)

# Lesson: best way to traverse through all directions.