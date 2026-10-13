class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        int lo = 1, hi = *max_element(begin(piles), end(piles));


        while (lo <= hi) {
            long long hours = 0;
            int k = (lo + hi) / 2;

            for (double i : piles) {
                hours += (i + k - 1)/ k;
            }

            if (hours <= h) hi = k - 1;
            else lo = k + 1;
        
        }
        return lo;
    }
};
