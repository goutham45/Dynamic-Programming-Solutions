def minSum (nums,n,sm):
    import sys
    t = [[-1 for x in range(sm+1)]for x in range(n+1)]

    for i in range(n+1):
        for j in range(sm+1):
            if i == 0:
                t[0][j] = False
            if j == 0:
                t[i][0] = True

    for i in range(1,n+1):
        for j in range(1,sm+1):
            if nums[i-1]<=j:
                t[i][j] = t[i-1][j-nums[i-1]] or t[i-1][j]
            elif nums[i-1]>j:
                t[i][j] = t[i-1][j]
    print(t[n])
    res = []
    x = sm//2
    for ele in range(x+1):
        if t[n][ele] == True:
            res.append(ele)

    minAns = 9223372036854775807
    for i in res:
        minAns = min(minAns,(sm-2*i))
    return minAns
nums=[1,1,2,3]
n = len(nums)
sm = 7
print(minSum(nums,n,sm))