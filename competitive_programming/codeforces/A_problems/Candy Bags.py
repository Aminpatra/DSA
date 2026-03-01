# http://codeforces.com/contest/334/problem/A

# Topic: implementation
# Rating: A: 1000

# Time took to solve problem is: 3 mins.
# Solved in First try.
# AI used ? No


n=int(input())
candies = [i for i in range(1, (n**2) + 1)]
l, r= 0, len(candies)-1
while l < r:
  print(candies[l], candies[r])
  l+=1
  r-=1
