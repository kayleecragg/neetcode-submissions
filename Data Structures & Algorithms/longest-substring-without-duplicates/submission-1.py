class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen, L = 0, 0
        seen = set()

        for R in range(len(s)):
            s[R]
            # set logic 
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            maxLen = max(R - L + 1, maxLen)
        
        return maxLen