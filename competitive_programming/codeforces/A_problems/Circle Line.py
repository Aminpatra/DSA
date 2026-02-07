# https://codeforces.com/contest/278/problem/A
# Topic: implementation
# Rating: A: 800

# Time took to solve problem is: 7 min.
# Solved in First try.
# AI used ? NO

n=int(input())
dists=list(map(int,input().split()))
s,t=map(int,input().split())
if s > t: s,t=t,s
print(min(sum(dists[s-1:t-1]), sum(dists)-sum(dists[s-1:t-1])))