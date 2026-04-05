class MinStack {
vector<int>newStack;
vector<int>minStack;

public:
    MinStack() {
    }
    
    void push(int val) {
        if (minStack.empty() || val <= minStack.back()) {
            minStack.push_back(val);
        }
        newStack.push_back(val);
    }
    
    void pop() {
        if (!minStack.empty() && newStack.back() == minStack.back()) {
            minStack.pop_back();
        }
        newStack.pop_back();
    }
    
    int top() {
        return newStack.back();  
    }
    
    int getMin() {

        // O(n) sol
        // auto min = 2000;
        // for (auto i : newStack) {
        //     if (i < min) {
        //         min = i;
        //     }
        // }
        // return min;

        // O(1) sol
        return minStack.back();
    }
};
