class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k>len(nums): return [] #always between 1<=k<=unique elements

        frqmap = {}
        for num in nums:
            if num not in frqmap:
                frqmap[num] = 1
            else:
                frqmap[num]+=1
        
        #get the nums with max count
        maxheap = [[-f, num] for num, f in frqmap.items()]
        heapq.heapify(maxheap)
        res = []
        while k>0:
            f, n = heapq.heappop(maxheap)
            res.append(n)
            k-=1
        return res


        #max a element can occur = len(nums)
        #least it can occur = 1
        # hashmap with values -> freq
        # keep track of max freq as we iterate through the array
        