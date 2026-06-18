class Solution:
    def scoreOfString(self, s: str) -> int:
        # assuming the length of the string is always even
        score, m = 0, 1
        for n in range(len(s) - 1):
            score += abs(ord(s[n]) - ord(s[m]))
            m += 1
        return score