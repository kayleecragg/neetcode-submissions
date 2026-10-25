class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set('aeiou')
        ans = ""

        for char in s:
            if char not in vowels:
                ans += char

        return ans

