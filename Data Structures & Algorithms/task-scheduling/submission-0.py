class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
        #build a frq map of the elements in tasks 
        #and push to the heap (freq, "task")
        #get the top element from heap
        #run through the keys in hashmap
        #as we run through the keys decrement counter, have dummy key -1:"idle"
        # frqmap = {"idle":0}
        # for task in tasks:
        #     frqmap[task] = 1+frqmap.get(task,0)
        
        # cycle = 0
        # #keep running through hashmap until all of them are zero
        # for task, count in frqmap.items():
        #     while count>0:
        #         if count!=0:
        #             count-=1
        #         elif count==0:
        #             continue