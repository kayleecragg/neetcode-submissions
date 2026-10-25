class Solution {
public:
    string removeVowels(string s) {
        string vowels = "aeiou";
        string ans = "";

        for (char c : s) if (vowels.find(c) == string::npos) ans += c;
        return ans;
    }
};
