class Solution:
    def findCoins(self, numWays):
        n = len(numWays)
        dp = [0] * (n + 1)
        dp[0] = 1
        ans = []

        for i in range(1, n + 1):
            if numWays[i - 1] < dp[i]:
                return []

            if numWays[i - 1] == dp[i]:
                continue

            if numWays[i - 1] != dp[i] + 1:
                return []

            ans.append(i)

            for j in range(i, n + 1):
                dp[j] += dp[j - i]

        return ans
