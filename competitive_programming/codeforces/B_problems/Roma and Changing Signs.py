# https://codeforces.com/contest/262/problem/B
# Topic: greedy
# Rating: 1200 B

# Time took to solve problem is: 30 min.
# Solved in Fourth try.
# AI used ? NO

n,k=map(int,input().split())
k_rem=k
income = list(map(int,input().split()))
for i in range(min(n,k)):
  if income[i] < 0: 
    income[i]*=-1
    k_rem-=1
if (k_rem & 1): 
  print(sum(income)- (2 * min(income)))
else: print(sum(income))

# Lesson: Getting the max sum if it is required to make k flips signs.