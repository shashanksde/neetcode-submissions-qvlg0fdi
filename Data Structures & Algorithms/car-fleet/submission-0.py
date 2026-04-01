class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)]
        pair.sort(reverse=True) #gives last position first

        stack = []
        for p,s in pair:
            stack.append((target-p)/s) #this gives time it will take to reach destination
            if len(stack)>=2 and stack[-1]<=stack[-2]: #there are atleast two elements to compare and 
                #the one on top is travelling at lower speed compared to one before it
                stack.pop()
        return len(stack)