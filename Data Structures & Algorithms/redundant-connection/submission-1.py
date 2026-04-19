class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N+1)] #will have parents as 1..N
        rank = [1]*(N+1) #N+1 because it is 1 indexed

        def find(n):
            if n!=par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1==p2:
                return False #this edge was already part of the group, that means
                #this is the redundant connection we were looking for
            
            if rank[p1]>rank[p2]:
                par[p2] = p1
                rank[p1]+=rank[p2]
            else:
                par[p1] = p2
                rank[p1]+=rank[p2]
            return True #turns out this edge was not part of the group and we just unified them

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        return []
            
