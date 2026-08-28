class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set() #this will contain the courses starting from a gven course
        def dfs(crs):
            if crs in visitSet: #we essentially reached the same course we started with, there is a cycle so cant complete
                return False
            if preMap[crs] == []: #if all of the pre-req is completed
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = [] #can complete all pre-requisites starting from this course. 
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): 
                return False
        return True



        
