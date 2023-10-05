def subset(arr,sum,n):
  t = [[0 for x in range(sum+1)] for x in range(n+1)]

  for i in range(n+1):
      for j in range(sum+1):
          if i == 0:
              t[0][j] = False
          if j == 0:
              t[i][0] = True

  for i in range(1,n+1):
    for j in range(1,sum+1):
      if arr[i-1]<=j:
        t[i][j] = (t[i-1][j - arr[i-1]] or t[i-1][j])
      elif arr[i-1]>j:
        t[i][j] = t[i-1][j]
  for row in t:
    print(row)
  return t[n][sum]

arr = [1,1,1,1,1]
sum = 3
n = len(arr)
print(subset(arr,sum,n))
