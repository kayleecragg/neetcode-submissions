class Solution {
public:
    bool isValid(string s) {
        vector<char>compiler; // make a vector of chars named compiler

        for (auto i : s) {

            if (i == '(' || i == '{' || i == '[') {
                compiler.push_back(i);
                continue;
            }

            if (i == ')') {
                if (compiler.empty() || compiler.back() != '(') return false;
                compiler.pop_back();
            }

            else if (i == '}') {
                if (compiler.empty() || compiler.back() != '{') return false;
                compiler.pop_back();
            }

            else if (i == ']') {
                if (compiler.empty() || compiler.back() != '[') return false;
                compiler.pop_back();
            }
        }

        // by end of loop if vector is not empty return false
        // otherwise return true

        if (!compiler.empty()) return false;
        return true;
    }   
};
