class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = [c.lower() for c in s if c.isalnum()]
        L, R = 0, len(cleaned) - 1

        while L < R:
            if cleaned[L] != cleaned[R]:
                return False

            L += 1
            R -= 1
        return True
        
        