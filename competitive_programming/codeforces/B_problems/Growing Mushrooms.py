# https://codeforces.com/contest/186/problem/B
# Topic: greedy/sorting
# Rating: 1200

# Time took to solve problem is: 28 min.
# Solved in Second try.
# AI used ? NO

n, t1, t2, per = map(int,input().split())
hash_map = []
for i in range(1, n+1):
  ai, bi = map(int,input().split())
  hash_map.append((i, max(((ai * t1 * (1-per/100)) + bi * t2), ((bi * t1 * (1-per/100)) + ai * t2))))

hash_map.sort(key=lambda x: (-x[1], x[0]))
for id, val in hash_map:
  print(id, f'{val:.2f}')

# Lesson: key=lambda x: (primary sorting, secondary if two are equal) you can add - sign before it to make largest first