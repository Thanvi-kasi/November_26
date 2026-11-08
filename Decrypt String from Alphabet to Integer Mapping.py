class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        i = len(s) - 1

        while i >= 0:
            if s[i] == '#':
                num = int(s[i - 2:i])
                ans.append(chr(96 + num))
                i -= 3
            else:
                num = int(s[i])
                ans.append(chr(96 + num))
                i -= 1

        return ''.join(ans[::-1])
