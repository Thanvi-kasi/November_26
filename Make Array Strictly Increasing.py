class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        from bisect import bisect_right

        arr2 = sorted(set(arr2))
        dp = { -1: 0 }

        for x in arr1:
            new_dp = {}

            for prev, cost in dp.items():
                if x > prev:
                    new_dp[x] = min(new_dp.get(x, float('inf')), cost)

                i = bisect_right(arr2, prev)

                if i < len(arr2):
                    y = arr2[i]
                    new_dp[y] = min(new_dp.get(y, float('inf')), cost + 1)

            dp = new_dp

            if not dp:
                return -1

        return min(dp.values())
