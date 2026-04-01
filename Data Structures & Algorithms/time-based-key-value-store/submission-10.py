class TimeMap:

    def __init__(self):
        self.emomap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.emomap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        '''
        if given timestamp is ahead of the time top of the stack we return whats on top
        else if its less than or equal to time on top we go
        '''
        res=""
        values = self.emomap.get(key,[])
        low = 0
        high = len(self.emomap[key])-1
        while low<=high:
            mid = (low+high)//2
            emo , time = self.emomap[key][mid]
            if time<=timestamp:
                res = emo
                low=mid+1
            else:
                high=mid-1
        
        return res
        

                                   

        
        
