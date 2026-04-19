class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        #create adjacency lis
        neiwords = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                neiwords[pattern].append(word)
        
        visit = set([beginWord])
        q = deque()
        q.append(beginWord)
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word==endWord: 
                    return res
                #create pattern for this word
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for n in neiwords[pattern]:
                        if n not in visit:
                            visit.add(n)
                            q.append(n)
            res+=1
        return 0



