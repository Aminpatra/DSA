# https://codeforces.com/contest/400/problem/B
# Topic: Implementation/brute force
# Rating: 1200

# Time took to solve problem is: 25 min.
# Solved in Second try.
# AI used ? "Yes" 'for a small hint' 

n, m=map(int,input().split())
dists=set()
for i in range(n):
  row = input()
  g = row.find('G')
  s = row.find('S')
  if s < g:
    print(-1)
    quit()
  dists.add(s-g)

print(len(dists))

# Lesson: Read the problem carefully.