x = "agbcdcbga"
n = len(x)
def lcs(x):
  y = x[::-1] # take the reverse of given string and compute palindromic subsequence
  m = len(y)
  t = [[0 for x in range(m+1)]for x in range(n+1)]
  for i in range(1,n+1):
    for j in range(1,m+1):
      if x[i-1] == y[j-1]:
        t[i][j] = 1 + t[i-1][j-1]
      else:
        t[i][j] = max(t[i][j-1], t[i-1][j])
  return t[n][m]
print(lcs(x))