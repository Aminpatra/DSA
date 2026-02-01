# https://codefoDreamoon and WiFirces.com/contest/129/problem/B
# Topic: Graphs

# time took to solve problem is: 30 min.
# solved in first try.
# AI used ? NO

n, m=map(int,input().split())
nodes = dict()
visited=set()
group=0
for i in range(m):
  a, b=map(int,input().split())
  if a in nodes: nodes[a].append(b)
  else: nodes[a] = [b]
  if b in nodes: nodes[b].append(a)
  else: nodes[b] = [a]

for i in range(n):
  f=False
  for node in nodes:
    if len(nodes[node]) == 1 and node not in visited:
      f=True
      nodes[nodes[node][0]].remove(node)
      visited.add(nodes[node][0])
      nodes[node] = []
  visited = set()
  if f:
    group += 1
  else: break

print(group)