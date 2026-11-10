class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        original = n
        multiplier = 1

        while sum(map(int, str(n))) > target:
            digit = (n // multiplier) % 10
            n += (10 - digit) * multiplier
            multiplier *= 10

        return n - original
