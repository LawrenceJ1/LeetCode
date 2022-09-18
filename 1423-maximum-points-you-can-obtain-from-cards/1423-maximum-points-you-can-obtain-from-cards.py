class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        front, back = [0], [0]
        for i in range(k):
            front.append(front[-1]+cardPoints[i])
            back.append(back[-1]+cardPoints[-i-1])
        front.append(0)
        back.append(0)
        for i in range(k+1):
            front[i] += back[k-i]
        return max(front)