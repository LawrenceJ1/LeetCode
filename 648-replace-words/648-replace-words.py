class TrieNode:
    def __init__(self):
        self.end = 0
        self.children = defaultdict(int)

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = pointer = TrieNode()
        for word in dictionary:
            for char in word:
                if not pointer.children[char]:
                    pointer.children[char] = TrieNode()
                pointer = pointer.children[char]
            pointer.end = 1
            pointer = root
        sentence = sentence.split()
        for word in range(len(sentence)):
            prefix = ''
            pointer = root
            for char in sentence[word]:
                if not pointer.children[char]:
                    pointer.children.pop(char)
                    break
                prefix += char
                pointer = pointer.children[char]
                if pointer.end:
                    sentence[word] = prefix
                    break
        return ' '.join(sentence)