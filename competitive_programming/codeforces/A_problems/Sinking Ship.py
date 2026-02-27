# https://codeforces.com/contest/63/problem/A

# Topic: implementation/strings
# Rating: A: 900

# Time took to solve problem is: 6 mins.
# Solved in First try.
# AI used ? No

n = int(input())
hash_map = {'rat': [], 'woman and child': [], 'man': [], 'captain': []}
for _ in range(n):
  crew_name, crew_status = input().split()
  if crew_status == 'woman' or crew_status == 'child':
    hash_map['woman and child'].append(crew_name)
  else: 
    hash_map[crew_status].append(crew_name)

for val in hash_map.values():
  for name in val: 
    print(name)