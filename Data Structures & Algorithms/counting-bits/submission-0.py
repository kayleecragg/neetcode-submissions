class Solution:
    def countBits(self, n: int) -> List[int]:
        
        output = [-1] * (n + 1)

        for i in range(n + 1):
            count = 0
            j = i

            while j > 0:
                if j & 1 == 1:
                    count += 1
                j = j >> 1
            
            output[i] = count

        return output
