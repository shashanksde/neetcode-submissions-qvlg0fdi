class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for ele in operations:
            if ele not in ["+","C","D"]:
                #number
                res.append(int(ele))
            elif ele=="+":
                first_ele, second_ele = res[-1], res[-2]
                new_ele = first_ele + second_ele
                res.append(new_ele)
            elif ele == "C":
                res.pop()
            elif ele == "D":
                top_ele = res[-1]
                new_ele = 2*top_ele
                res.append(new_ele)
        
        return sum(res)