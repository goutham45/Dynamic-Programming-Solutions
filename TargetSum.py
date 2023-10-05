def findTargetSumWays(self, nums: List[int], target: int) -> int:
    n = len(nums)
    sm = sum(nums)
    if target+sm < 0:
        return 0
    if (sm+target)%2!=0:
        return 0
    s1 = (sm + target) // 2
    target = s1 
    t = [[0 for x in range(target+1)] for x in range(n+1)]
    t[0][0] = 1
    # for i in range(n+1):
    #     for j in range(target+1):
    #         if j == 0:
    #             t[i][j] = 1

    for i in range(1,n+1):
        for j in range(target+1):
            if nums[i-1]<=j:
                t[i][j] = (t[i-1][j - nums[i-1]] + t[i-1][j])
            elif nums[i-1]>j:
                t[i][j] = t[i-1][j]
    # for row in t:
    #     print(row)
    return t[n][target]
