class TrieNode:
    def __init__(self):
        self.end = 0
        self.children = defaultdict(str)

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        pointer = self.root
        for char in word:
            if not pointer.children[char]:
                pointer.children[char] = TrieNode()
            pointer = pointer.children[char]
        pointer.end = 1

    def search(self, word: str) -> bool:
        pointer = self.root
        for char in word:
            if not pointer.children[char]:
                return False
            pointer = pointer.children[char]
        return pointer.end
        
    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for char in prefix:
            if not pointer.children[char]:
                return False
            pointer = pointer.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)