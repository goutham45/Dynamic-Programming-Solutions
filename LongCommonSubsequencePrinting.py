def lcs(x,y,n,m):
  t = [[0 for x in range(m+1)] for x in range(n+1)]
  for i in range(1,n+1):
    for j in range(1,m+1):
      if x[i-1] == y [j-1]:
        t[i][j] = 1 + t[i-1][j-1]
      else:
        t[i][j] = max(t[i-1][j], t[i][j-1])
  for i in t:
    print(i)
    
  e = n
  f = m
  res = ""
  while e>0 and m>0:
    if x[e-1] == y[f-1]:
      res+=x[e-1]
      e-=1
      f-=1
    else:
      if t[e-1][f]>t[e][f-1]:
        e-=1
      else:
        f-=1
  return res[::-1]

x = "xyasgc"
y = "xyadgc"
n = len(x)
m = len(y)
lcs(x,y,n,m)