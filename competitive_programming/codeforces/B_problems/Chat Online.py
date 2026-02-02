# https://codeforces.com/contest/469/problem/B
# Topic: implementation
# Rating: 1300

# Time took to solve problem is: 45 min.
# Solved in fourth try.
# AI used ? YES 'Only for small hints'

p,q,l,r=map(int,input().split())
moments=0
Z=[]
A=[]
for i in range(p):
  Z.append([*map(int,input().split())])
for i in range(q):
  A.append([*map(int,input().split())])

for t in range(l, r+1):
  f=False
  for a_time in A:
    for z_time in Z:
      if (a_time[0]+t >= z_time[0] and a_time[0]+t <= z_time[1]) \
      or (a_time[1]+t >= z_time[0] and a_time[1]+t <= z_time[1]) \
      or (a_time[0]+t < z_time[0] and a_time[1]+t > z_time[1]):
        f=True
        break
    if f:
      moments+=1
      break
print(moments)

# lesson: Think about all possible cases before you jump to implementing the code

# past solution: 
p,q,l,r = map(int,input().split())
z=[]
x=[]

for i in range(p): z.append([*map(int, input().split())])
for i in range(q): x.append([*map(int, input().split())])

valid_t = set()

for t in range(l, r + 1):
  found = False
  for cx, dx in x:
    shifted_c, shifted_d = cx + t, dx + t
    for az, bz in z:
      if not (shifted_d < az or shifted_c > bz):
        valid_t.add(t)
        found = True
        break
    if found:
      break

print(len(valid_t))