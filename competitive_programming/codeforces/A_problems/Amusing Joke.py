# http://codeforces.com/contest/141/problem/A

# Topic: implementation/brute force
# Rating: A: 800

# Time took to solve problem is: 5 mins.
# Solved in First try.
# AI used ? No

# First solution

s1=input()
s2=input()
pile=input()
print('YES' if sorted(s1+s2) == sorted(pile) else "NO")


# Second solution

# from sys import stdin
from collections import Counter

s1 = Counter(input())
s2 = Counter(input())
pile = Counter(input())

for l1 in s1: 
  if (l1 not in pile):
    print("NO")
    exit()
  pile[l1] -= s1[l1]

for l2 in s2: 
  if (l2 not in pile):
    print("NO")
    exit()
  pile[l2] -= s2[l2]

for val in pile.values():
  if (val != 0):
    print("NO")
    exit()

print("YES")