# https://codeforces.com/contest/385/problem/B
# Topic: greedy/implementation/math/strings/brute force
# Rating: B: 1200

# Time took to solve problem is: 1 hour.
# Solved in Second try.
# AI used ? Yes (to know what was wrong with the first solution)

s=input()
l=len(s)
bear_positions=[]
for i in range(l-3):
  if (s[i:i+4] == 'bear'):
    bear_positions.append(i)

if bear_positions: 
  t=0
  for i in range(l):
    first_bear=None
    for pos in bear_positions:
      if pos >= i: 
        first_bear = pos
        break
    if first_bear is not None:
      t += l - (first_bear + 3)
  print(t)
else: 
  print(0)
