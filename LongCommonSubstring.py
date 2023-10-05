x = "abcd"
y = "abc"
n = len(x)
m = len(y)

def lcs(x,y,n,m):
    res = 0
    t= [[0 for x in range(m+1)] for x in range(n+1)]
    for i in range(1,n+1):
      for j in range(1,m+1):
        if x[i-1] == y[j-1]:
          t[i][j] = 1 + t[i-1][j-1]
          res = max(res,t[i][j])
        else:
          t[i][j] = 0
          # t[i][j] = max(t[i][j-1], t[i-1][j]) 
    for row in t:
      print(row)
    return res
print(lcs(x,y,n,m))