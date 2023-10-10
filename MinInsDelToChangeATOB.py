def lcs(x,y,n,m):
  t = [[0 for x in range(m+1)] for x in range(n+1)]
  for i in range(1,n+1):
    for j in range(1,m+1):
      if x[i-1] == y[j-1]:
        t[i][j] = 1 + t[i-1][j-1]
      else:
        t[i][j] = max(t[i][j-1],t[i-1][j])
  insertion = len(y) - t[n][m]
  deletion = len(x) - t[n][m]
  return [insertion, deletion]
  
x = "axypqc"
y = "xybf"
n = len(x)
m = len(y)
insDel = lcs(x,y,n,m)
print("The number of char to be inserted is {0} and deleted is {1}".format(insDel[0],insDel[1]))