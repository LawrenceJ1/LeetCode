class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        queue = deque()
        queue.append(beginWord)
        visited = set()
        words = set(wordList)
        count = 2
        x = len(beginWord)
        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                temp = queue.popleft()
                for i in range(x):
                    for j in range(97, 123):
                        word = list(temp)
                        word[i] = chr(j)
                        word = "".join(word)
                        if word not in visited and word in words:
                            if word == endWord:
                                return count
                            queue.append(word)
                            visited.add(word)
            count += 1
        return 0