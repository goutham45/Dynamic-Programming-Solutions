length = [1,2,3,4,5,6,7,8]
price = [1,5,8,9,10,17,17,20]
n = len(length)

def ukRod(length,price,n):
  t= [[0 for x in range(n+1)] for x in range(n+1)]

  for i in range(n+1):
    for j in range(n+1):
      if j == 0:
        t[i][j] = 0
      if length[i-1]<=j:
        t[i][j] = max(price[i-1] + t[i][j-length[i-1]], t[i-1][j])
      elif length[i-1]>j:
        t[i][j] = t[i-1][j]
  for row in t:
    print(row)
  return t[i][j]

print(ukRod(length,price,n))


