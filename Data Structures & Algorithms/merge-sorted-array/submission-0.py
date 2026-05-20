class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        o = m + n
        nums3 = [0] * o

        i, num1p, num2p = 0, 0, 0

        while num1p < m and num2p < n:
            if nums1[num1p] <= nums2[num2p]:
                nums3[i] = nums1[num1p]
                num1p += 1

            else:
                nums3[i] = nums2[num2p]
                num2p += 1

            i += 1
            

        while num1p < m:
            nums3[i] = nums1[num1p]
            num1p += 1
            i += 1

        while num2p < n:
            nums3[i] = nums2[num2p]
            num2p += 1
            i += 1

        for i in range(len(nums3)):
            nums1[i] = nums3[i]

