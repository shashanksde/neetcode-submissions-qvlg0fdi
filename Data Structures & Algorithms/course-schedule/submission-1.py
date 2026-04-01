class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)

        visited = set()
        def dfs(crs):
            #we have seen this crs earlier already
            if crs in visited:
                return False
            
            #its a dead end and can be completed
            if premap[crs]==[]:
                return True
            
            visited.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            #we remove to tell that we know this crs can be reached
            visited.remove(crs)
            premap[crs]=[] #tells no need to 

            return True

        #need to iterate through all values because
        #graphs can be disconnected.
        for crs in range(numCourses):
            if not dfs(crs): return False

        return True


        