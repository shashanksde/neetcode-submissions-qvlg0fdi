class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in cars:
            time_taken = (target-p)/s
            if not stack or time_taken > stack[-1]:
                stack.append(time_taken)
        
        return len(stack)