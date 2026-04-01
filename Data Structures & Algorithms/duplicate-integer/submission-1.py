class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


'''
explore:
1. can there be just one or no elements in the list
2. can there be more than one occurence of a number.
3. Can there me more than one duplicate

brainstorm:
1st approach: sort the array, check if arr[i]==arr[i+1]
TC: O(nlogn) SC: O(1)

2nd approach: keep adding elements to a set, if a element already in a set
return True immediately
TC: O(n) SC: O(n)

3rd approach:
check if length of the list would be equal to len of its set
TC: O(n) SC: O(n)



'''