class Solution {
public:
    int lengthOfLastWord(string s) {
        auto wordlength = 0, lastwordlength = 0;
        auto hi = s.length();

        for (auto i = 0; i < hi; i++) {
            // if the character is a space, bring wordlength back to 0
            if (s[i] == ' ') {
                if (wordlength != 0) lastwordlength = wordlength;
                wordlength = 0;
            }
            else {
                wordlength++;
            }

            // if its the last character?
            if (i == hi - 1) {
                if (wordlength == 0) {
                    return lastwordlength;
                }
                else {
                    return wordlength;
                }
            }
        }
    }
};