class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      #i will need a min heap do -n of nums
      #then until count<k pop elements
      #return the positive value
      nums = [-n for n in nums]
      heapq.heapify(nums)
      
      res = 0
      while k>0:
        res = heapq.heappop(nums)
        k-=1
      return -res #dont forget to negate , if it was negative number it was positive in the heap