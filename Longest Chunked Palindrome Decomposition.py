class Solution:
    def longestDecomposition(self, text: str) -> int:
        left, right = 0, len(text) - 1
        prefix, suffix = "", ""
        ans = 0

        while left < right:
            prefix += text[left]
            suffix = text[right] + suffix

            if prefix == suffix:
                ans += 2
                prefix = ""
                suffix = ""

            left += 1
            right -= 1

        # Count the remaining middle character or substring
        if left == right or prefix:
            ans += 1

        return ans
