class Solution {
public:
    int lengthOfLastWord(string s) {
        auto wordlength = 0, lastwordlength = 0;

        for (auto i = 0; i < s.length(); i++) {
            // if the character is a space, bring wordlength back to 0
            if (s[i] == ' ') {
                if (wordlength != 0) lastwordlength = wordlength;
                wordlength = 0;
            }
            else {
                wordlength++;
            }
        }

        return wordlength ==0 ? lastwordlength : wordlength;
    }
};