class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endofword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #build a Trie
        t = TrieNode()
        for word in words:
            t.insert(word)
        
       
        ROWS , COLS = len(board), len(board[0])
        res, visit = set(), set()
        #now do a dfs on the board see if a character at a cell is one of the children from the root
        #if so go dfs on all 4 directions, until we cant find a word
        #our output will contain the final set of words found 
        def dfs(r, c, node, word):
            #base case, out of bounds
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or (r, c) in visit or
                board[r][c] not in node.children):
                return

            visit.add((r,c))
            node = node.children[board[r][c]] #this child node becomes new cur pointer
            word+=board[r][c] #form the word in this search
            if node.endofword: #if by here we reached end of word by adding a char, add to result
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
            
        for r in range(ROWS):
            for c in range(COLS):
                #check if this char is one of the children from root
                #if so proceed with dfs
                dfs(r, c, t, "")
        return list(res)

