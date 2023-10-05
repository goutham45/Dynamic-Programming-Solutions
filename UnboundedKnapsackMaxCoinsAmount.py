def change(self, amount: int, coins: List[int]) -> int:
    n = len(coins)
    # if sum(coins) < amount:
    #     return -1

    def coinChange(coins,amount,n):
        t = [[0 for i in range(amount+1)] for i in range(n+1)]

        for i in range(n+1):
            for j in range(amount+1):
                if j==0:
                    t[i][j] = 1

        for i in range(1,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    # t[i][j] = min(t[i][j],t[i][j-coins[i-1]]+ t[i-1][j])
                    t[i][j] = t[i][j-coins[i-1]]+ t[i-1][j]
                elif coins[i-1]>j:
                    t[i][j] = t[i-1][j]
        for row in t:
            print(row)
        
        return t[n][amount]
    
    return coinChange(coins,amount,n)