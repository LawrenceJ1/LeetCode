class TrieNode:
    def __init__(self):
        self.children = defaultdict(int)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        root = TrieNode()
        l = len(bin(max(nums)))-2
        for num in nums:
            temp = f'{num:0{l}b}'
            pointer = root
            for i in range(len(temp)):
                if not pointer.children[temp[i]]:
                    pointer.children[temp[i]] = TrieNode()
                pointer = pointer.children[temp[i]]
        self.ans = 0
        x = y = root.children['1']
        val = (2**(l-1))-1
        if root.children['0']:
            val = (2**l)-1
            y = root.children['0']
        def recursive(pointer1, pointer2, val, index):
            if index == 0:
                self.ans = max(self.ans, val)
                return
            if val < self.ans:
                return
            if pointer1.children['1'] and pointer2.children['0']:
                recursive(pointer1.children['1'], pointer2.children['0'], val, index-1)
            if pointer1.children['0'] and pointer2.children['1']:
                recursive(pointer1.children['0'], pointer2.children['1'], val, index-1)
            if pointer1.children['1'] and pointer2.children['1']:
                recursive(pointer1.children['1'], pointer2.children['1'], val-2**(index-1), index-1)
            if pointer1.children['0'] and pointer2.children['0']:
                recursive(pointer1.children['0'], pointer2.children['0'], val-2**(index-1), index-1)
        recursive(x, y, val, l-1)
        return self.ans