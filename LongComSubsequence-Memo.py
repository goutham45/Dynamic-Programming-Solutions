def lcs(x,y,n,m):
  t = [[-1 for x in range(m+1)] for x in range(n+1)]
  for i in t:
    print(i)
  for i in range(n+1):
    for j in range(m+1):
      if i == 0 or j == 0:
        return 0
      elif t[i][j] != -1:
        return t[i][j]
      else:
          if x[i-1] == y[j-1]:
            t[i][j] = 1+lcs(x,y,i-1,j-1)
            return t[i][j]
          else:
            t[i][j] = max(lcs(x,y,i,j-1),lcs(x,y,i-1,j))
            return t[i][j]


x = "ylqpejqbalahwr"
y = "yrkzavgdmdgtqpg"
n = len(x)
m = len(y)
lcs(x,y,n,m)
