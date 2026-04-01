class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True #empty tree
        
        #remember this one is undirected graph so edge is bi-directional from n1-n2
        adjList = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        

        visit = set() 
        def dfs(i,prev):
            if i in visit: #if we somehow come to the one which we already visited that means there is a cycle and not a tree
                return False
            
            visit.add(i)
            for n in adjList[i]:
                if n==prev: #going back to the same node where we came from
                    continue
                if not dfs(n,i): #if starting at this node and prev as the one we came from, if this is false that means 
                    return False
            return True
        
        return dfs(0,-1) and n==len(visit)