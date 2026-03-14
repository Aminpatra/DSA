# https://codeforces.com/contest/670/problem/A
# Topic: constructive algorithms/math
# Rating: A: 900

# Time took to solve problem is: 10 min.
# Solved in Second try.
# AI used ? 


n=int(input())
weeks= n//7
rem = n % 7

base = weeks * 2
min_days = base + max(0, rem-5)
max_days = base + min(2, rem)

print(min_days, max_days)