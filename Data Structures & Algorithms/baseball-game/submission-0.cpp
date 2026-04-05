class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int>newStack;
        for (auto i : operations) {
            if (i != "+" && i != "C" && i != "D") {
                newStack.push_back(stoi(i));
                continue;
            }

            if (i == "C") {
                newStack.pop_back();
            }

            else if (i == "+") {
                // add the last two elements in the stack
                if ((int)newStack.size() > 1) {
                    int last = newStack.back();
                    int secondLast = newStack[(int)newStack.size() - 2];
                    newStack.push_back(last + secondLast);
                }
            }

            else if (i == "D") {
                // double the last element of the stack;
                int last = newStack.back();
                newStack.push_back(last * 2);
            }
        } 
        auto sum = 0;
        for (auto h : newStack) {
            sum+=h;
        }
        return sum;
    }
};