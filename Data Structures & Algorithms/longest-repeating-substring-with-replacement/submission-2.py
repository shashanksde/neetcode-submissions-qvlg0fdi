class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #needed to store the frequency of the all the characters
        res = 0

        l = 0
        maxf = 0 #this optimization technique is to get the most frequent number in O(1) time
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) #this gets the max frequency in O(1) time

            while (r - l + 1) - maxf > k: #here we see if window size - max frequency > number of replacements that can be made
                count[s[l]] -= 1 #make it valid by removing the left most character
                l += 1 #and move the pointer towards the right
            res = max(res, r - l + 1) #get the size of the valid window 

        return res




        #iterate through the string if they are not in seen set
        #decrement k
        #i can keep expanding my window until k reaches 0
        #once k is 0 I need to make the window valid again so remove from left
        #take max window length along the process

