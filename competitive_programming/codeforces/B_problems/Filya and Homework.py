# https://codeforces.com/contest/714/problem/B
# Topic: Implementation/Sorting
# Rating: 1200

# Time took to solve problem is: 40 min.
# Solved in Third try.
# AI used ? "Yes" 'for a small hint after 30 min thinking' 

int(input())
arr=sorted(list(set(map(int,input().split()))))
if len(arr) > 3: print("NO")
elif len(arr) == 1 or len(arr) == 2: print("YES")
else: 
  if (arr[2]-arr[1] == arr[1]-arr[0]):
    print("YES")
  else: print("NO")

# Lessons: to make all elements of an array equal by choosing an x integer
# this x can be subtracted or added only once or we leave the element, then they must from an arithmetic sequence
# if we have a < b < c, if we want to check for arithmetic seq: b * 2 = a + c