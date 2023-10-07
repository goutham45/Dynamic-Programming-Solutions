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
  return n+m-t[n][m] ## so the shortest sequence will be addition of length of 2 strings minus the Longest common subsequence

x = "xyzeasef"
y = "xyzedjhf"
n = len(x)
m = len(y)
lcs(x,y,n,m)