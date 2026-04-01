class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #prepare a hashmap with val->count
        #until k values return the highest count values
        from collections import defaultdict
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] +=1
        
        res = []
        for num, count in sorted(countMap.items(), key=lambda item: item[1], reverse=True):
            res.append(num)
            k-=1
            if k==0:
                break
        return res