n,m=map(int,input().split())
xc, yc= map(int,input().split())
k=int(input())
moves=0
for _ in range(k):
  dx, dy =map(int,input().split())

  if (dx > 0 and dy > 0):
    x_dist = ((n-xc) // dx) * dx
    y_dist = ((m-yc) // dy) * dy
    # m_dist = min(x_dist, y_dist)
    if ((xc+x_dist <= n and xc+x_dist > 0) and (yc+y_dist <= m and yc+y_dist > 0)):
      xc += x_dist
      yc += y_dist
      moves += min(x_dist, y_dist)
    # # print((n-xc) // dx, 'here')
    # if (x_dist <= y_dist):
    #   moves += (n-xc) // dx
    #   xc += x_dist
    #   yc += x_dist
    # else: 
    #   moves += (m-yc) // dy
    #   xc += y_dist
    #   yc += y_dist

  else: continue

print(moves, xc, yc)
