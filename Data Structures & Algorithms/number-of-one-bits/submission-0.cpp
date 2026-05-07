class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        for (int i = 31; i >= 0; i--) {
            uint32_t mask = 1u << i;
            uint32_t res = n & mask;
            res = res >> i;
            if (res == 1) count++;
        }

        return count;

    }
};
