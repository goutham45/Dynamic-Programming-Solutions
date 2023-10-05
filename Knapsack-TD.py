def knapsack1(wt,val,W,n):
  t = [[-1 for x in range(W + 1)] for x in range(n + 1)]
  # print("hi")
  for i in range(n+1):
    for w in range(W+1):
      if i == 0 or w==0:
        t[i][w] = 0
      elif wt[i-1]<=w:
        t[i][w] = max(val[i-1] + t[i-1][w - wt[i-1]] , t[i-1][w])
      else:
        t[i][w] = t[i-1][w]
  return t[n][W]

profit = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(profit)
print(knapsack1(wt, profit, W, n))