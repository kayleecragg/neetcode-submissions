class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # two pass
        # from i to end of array
        for i in range(len(arr)):
            # from j (i + 1) to end of array (all to the right)
            biggest = -1
            for j in range(i + 1, len(arr)):
                biggest = max(arr[j], biggest)
            arr[i] = biggest

        return arr
