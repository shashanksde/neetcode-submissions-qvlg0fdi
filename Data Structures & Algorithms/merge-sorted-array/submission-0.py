class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pt1,pt2,pt_to_swap = m-1,n-1,m+n-1
        #go until index is 0 in either of these arrays
        while pt1 >= 0 and pt2 >= 0:
            if nums1[pt1] <= nums2[pt2]:
                nums1[pt_to_swap] = nums2[pt2]
                pt2-=1
            else:
                nums1[pt_to_swap] = nums1[pt1]
                pt1-=1
            
            pt_to_swap-=1
        
        while pt2 >= 0:
            nums1[pt_to_swap] = nums2[pt2]
            pt2 -= 1
            pt_to_swap -= 1