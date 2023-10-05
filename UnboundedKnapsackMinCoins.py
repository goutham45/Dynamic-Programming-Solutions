def MinCoins(coins):
    n = len(coins)
    t = [[-1 for i in range(amount+1)] for j in range(n+1)]
    for i in range(n+1):
        t[i][0] = 0
        for j in range(1,amount+1):
            t[0][j] = amount+1

    for i in range(1,n+1):
        for j in range(1,amount+1):
            if coins[i-1]<=j:
                t[i][j] = min(t[i-1][j],t[i][j-coins[i-1]]+ 1)
            elif coins[i-1]>j:
                t[i][j] = t[i-1][j]

    return -1 if t[n][amount] > amount else t[n][amount]