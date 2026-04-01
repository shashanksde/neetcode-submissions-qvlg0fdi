class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return n #empty tree
        
        #remember this one is undirected graph so edge is bi-directional from n1-n2
        adjList = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        

        visit = set() 
        def dfs(i):
            if i in visit:
                return 0
            visit.add(i)
            for j in adjList[i]:
                if j in visit:
                    continue
                dfs(j)
            return 1
        
        count = 0
        for i in range(n):
            if dfs(i):
                count+=1
        
        return count
