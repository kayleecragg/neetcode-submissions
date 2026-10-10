class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        for (auto i = 0; i < arr.size() - 1; i++) {
            auto biggest = 0;
            for (auto j = i + 1; j < arr.size(); j++) {
                biggest = max(biggest, arr[j]);
            }
            arr[i] = biggest;
        }

        arr[arr.size() - 1] = -1; // last element w -1
        return arr;
    }
};