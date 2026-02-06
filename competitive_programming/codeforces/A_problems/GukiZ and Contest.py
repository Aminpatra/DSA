n=int(input())
v=list(map(int,input().split()))
hast_map = {}
for i in range(n):
  if v[i] not in hast_map:
    hast_map[v[i]] = 1
    for j in range(n):
      if v[j] > v[i]:
        hast_map[v[i]] += 1
for i in range(n):
  print(hast_map[v[i]], end=" ")