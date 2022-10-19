class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
        for word in words:
            d[word] += 1
        return [k for k, _ in sorted(d.items(), key=lambda x: (-x[1], x[0]))][:k]