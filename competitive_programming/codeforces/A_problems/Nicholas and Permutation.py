# https://codeforces.com/contest/676/problem/A

# Topic: constructive algorithms
# Rating: A: 800

# Time took to solve problem is: 10 mins.
# Solved in Third try.
# AI used ? No

n=int(input())
nums=list(map(int,input().split()))
mn,mx=nums[0], nums[0]
mn_pos, mx_pos = 0, 0
for i in range(n):
  if (nums[i] > mx):
    mx = nums[i]
    mx_pos = i
  if (nums[i] < mn):
    mn = nums[i]
    mn_pos = i

print(max(abs(mn_pos - n)-1, mn_pos, abs(mx_pos - n)-1, mx_pos))