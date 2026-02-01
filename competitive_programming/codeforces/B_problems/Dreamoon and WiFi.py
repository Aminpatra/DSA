# https://codeforces.com/contest/476/problem/B
# Topic: Math/Combinations

# time took to solve problem is: 35 min.
# solved in first try.
# AI used ? NO

from math import factorial
from collections import Counter
s1, s2 = Counter(input()), Counter(input())
if '?' not in s2:
  if (s1.get('+') == s2.get('+')) and (s1.get('-') == s2.get('-')): print(float(1))
  else: print(float(0))
else: 
  pos = s1.get('+', 0) - s2.get('+', 0)
  neg = s1.get('-', 0) - s2.get('-', 0)
  if (pos < 0) or (neg < 0): print(float(0))
  else: 
    n=s2['?']
    r=max(pos, neg)
    print((factorial(n) / (factorial(r) * factorial((n-r))))/2**n)

# Lessons : n!/r! * (n-r)! to get the total comb of a state.
