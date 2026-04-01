class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #add -val of stones to heap
        if len(stones)==0: return 0
        if len(stones)==1: return 1
        stones =[-x for x in stones]
        heapq.heapify(stones)
        
        #do these until atleast two stones are available to smash
        while len(stones)>=2:
            #x will be least value y will second least val
            x , y = heapq.heappop(stones), heapq.heappop(stones)

            if x!=y:
                posx, posy = -x, -y
                if posx<posy:
                    neww = posy - posx
                    heapq.heappush(stones, -neww)
                elif posx>posy:
                    neww = posx-posy
                    heapq.heappush(stones, -neww)
        if len(stones)==1:
            val = heapq.heappop(stones)
            return -val
        else:
            return 0
