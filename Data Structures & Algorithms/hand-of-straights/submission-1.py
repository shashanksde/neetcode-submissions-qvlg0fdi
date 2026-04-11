class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        
        count = defaultdict(int)
        for n in hand:
            count[n]+=1
        
        minH = list(count.keys()) #the unique numbers in hand
        heapq.heapify(minH)

        while minH:
            first = minH[0] #the top most minimum element in the heap

            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i] == 0: #if the count becomes zero but it is not the minimum element 
                    if i!=minH[0]:#then it is not the beginning of the group
                        return False
                    heapq.heappop(minH)
        return True
