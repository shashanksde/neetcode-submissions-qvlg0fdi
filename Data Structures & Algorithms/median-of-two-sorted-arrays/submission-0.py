class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        res.extend(nums1)
        res.extend(nums2)
        res.sort()

        length = len(res)
        if length%2==0:
            middle = length//2
            median = (res[middle]+res[middle-1])/2
            return median
        else:
            middle = length//2
            return float(res[middle])