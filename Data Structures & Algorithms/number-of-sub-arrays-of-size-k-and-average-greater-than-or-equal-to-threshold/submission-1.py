class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L, totalNum, averageSum = 0, 0, 0
        for R in range(len(arr)):
            # add right pointer value to sum
            averageSum += arr[R]
            # if the window is size k
            if R - L + 1 == k:
                # and the average is greater than or equal to threshold
                if (averageSum / k) >= threshold:
                    totalNum += 1
                averageSum -= arr[L]
                L += 1
                # if the average is not greater than or equal, 
                # means window has to move
        return totalNum
