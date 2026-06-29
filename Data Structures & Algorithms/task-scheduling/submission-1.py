class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqmap = defaultdict(int)

        for task in tasks:
            freqmap[task] = 1+freqmap.get(task,0)
        
        maxheap = []
        heapq.heapify(maxheap)
        for freq in freqmap.values():
            heapq.heappush(maxheap, -freq)

        q = deque() #pairs of [-cnt, time the task will be available]
        time = 0
        while maxheap or q:
            time+=1
            if maxheap:
                cnt  = 1+heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1]==time: #the front of the queue can now be processed
                heapq.heappush(maxheap, q.popleft()[0])
        return time            
            