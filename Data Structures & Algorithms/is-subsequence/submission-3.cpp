class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (!t.size() and s.size() > 0) return false; // edge case
        if (s.size() == 0) return true; // edge case?

        int i = 0, j = 0;
        while (i < t.size()) {
            if (t[i] == s[j]) j++;
            i++;
        }

        if (j < s.size()) return false;
        return true;
    }
};