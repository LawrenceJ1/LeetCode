class TrieNode:
    def __init__(self):
        self.val = 0
        self.children = defaultdict(str)

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        pointer = self.root
        for char in key:
            if not pointer.children[char]:
                pointer.children[char] = TrieNode()
            pointer = pointer.children[char]
        pointer.val = val

    def sum(self, prefix: str) -> int:
        pointer = self.root
        for char in prefix:
            if not pointer.children[char]:
                pointer.children.pop(char)
                return 0
            pointer = pointer.children[char]
        self.ans = 0
        def dfs(node):
            for key in node.children:
                dfs(node.children[key])
            self.ans += node.val
        dfs(pointer)
        return self.ans

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)