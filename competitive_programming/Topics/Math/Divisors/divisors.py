n = int(input())
divisors = []
i = 1

while i * i <= n:
  if (n % i == 0):
    divisors.append(i)
    if (n // i != i):
      divisors.append(n//i)
  i += 1

print(*divisors)


# Solving Problems

n, k = map(int,input().split())
# divisors = []
a, b = [], []

i = 1
while i * i <= n:
  if (n % i == 0):
    a.append(i)
    if (n // i != i):
      b.append(n//i)
  i += 1

if k > len(a) + len(b):
  print(-1)
else:
  if k > len(a):
    print(sorted(b)[k-len(a)-1])
  else: 
    print(a[k-1])

#######################################################

# https://cses.fi/problemset/task/1713/

n = int(input())
queries = [int(input()) for _ in range(n)]

MAX_X = 10**6
divs = [0] * (MAX_X + 1)

for i in range(1, MAX_X + 1):
  for j in range(i, MAX_X + 1, i):
    divs[j] += 1

for x in queries:
  print(divs[x])

#######################################################

# https://codeforces.com/problemset/problem/1294/C

from itertools import permutations

for _ in range(int(input())):
  n = int(input())
  divisors = []

  i = 1
  while i * i <= n:
    if (n % i == 0):
      divisors.append(i)
      if (n // i != i):
        divisors.append(n//i)
    i += 1

  f = False
  a, b, c = 0, 0, 0
  for per in permutations(divisors[2:], 3):
    if (per[0] * per[1] * per[2] == n):
      a, b, c = per[0], per[1], per[2]
      f = True
      break
  if f: 
    print("YES")
    print(a, b, c)
  else: print("NO")

