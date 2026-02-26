# http://codeforces.com/contest/401/problem/A

# Topic: implementation/math
# Rating: A: 800

# Time took to solve problem is: 6 mins.
# Solved in First try.
# AI used ? No

n, x=map(int,input().split())
cards_sum = abs(sum(map(int,input().split())))
need = 0
while cards_sum > 0:
  cards_sum -= x
  need += 1
print(need)