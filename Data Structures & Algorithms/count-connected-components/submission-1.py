class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)] #initially each node is a parent of itself
        rank = [1]*n #each node will have a size of 1 initially

        def find(node):
            res = node
            #this loop runs until it finds the root node of the links
            while res != parent[res]:
                parent[res] = parent[parent[res]] #path compression, go directly to grand parent
                res = parent[res]

            return res

        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)

            #if they belong to the same group they will have same root parent
            if parent1 == parent2:
                return 0

            if rank[parent2]>rank[parent1]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1] #the size of parent2 grows
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2] #the size of parent1 grows
            return 1 #we just clubbed them together and made one component


        res = n
        for n1, n2 in edges:
            res-=union(n1,n2)
        return res
