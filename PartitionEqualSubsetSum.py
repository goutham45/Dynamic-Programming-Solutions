def Ps(nums)  :
    def subset(nums,sm,n):
            t = [[-1 for x in range(sm+1)] for x in range(n+1)]
            for i in range(n+1):
                for j in range(sum+1):
                    if i == 0:
                        t[0][j] = False
                    if j == 0:
                        t[i][0] = True

            for i in range(1,n+1):
                for j in range(1,sm+1):
                    if nums[i-1]<=j:
                        t[i][j] = (t[i-1][j-nums[i-1]] or t[i-1][j])
                    elif nums[i-1]>j:
                        t[i][j] = t[i-1][j]
            return t[n][sm]

    totSum = sum(nums)
    n = len(nums)
    if (totSum % 2) == 0:
        sm = totSum //2
        return subset(nums,sm,n)
    else:
        return False


