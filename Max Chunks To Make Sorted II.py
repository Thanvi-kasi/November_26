class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)

        suffix_min = [0] * n
        suffix_min[n - 1] = arr[n - 1]

        # Calculate suffix minimum
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(arr[i], suffix_min[i + 1])

        chunks = 0
        prefix_max = float('-inf')

        # Find valid partition points
        for i in range(n):
            prefix_max = max(prefix_max, arr[i])

            if i == n - 1 or prefix_max <= suffix_min[i + 1]:
                chunks += 1

        return chunks
