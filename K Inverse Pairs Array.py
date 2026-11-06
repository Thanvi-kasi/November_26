class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            new = [0] * (k + 1)
            window = 0

            for j in range(k + 1):
                window += dp[j]

                if j >= i:
                    window -= dp[j - i]

                window %= MOD
                new[j] = window

            dp = new

        return dp[k]
