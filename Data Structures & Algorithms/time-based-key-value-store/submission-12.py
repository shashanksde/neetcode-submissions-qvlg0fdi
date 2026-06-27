class TimeMap:

    def __init__(self):
        #set key value pair "name":[[time, "value"]....]
        self.namemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.namemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.namemap[key])-1
        res = ""
        while l<=r:
            mid = (l+r)//2
            time, val = self.namemap[key][mid]
            if time<=timestamp:
                res = val
                l = mid+1
            else:
                r = mid-1
        return res
