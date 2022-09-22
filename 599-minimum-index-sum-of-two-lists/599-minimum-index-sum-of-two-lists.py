class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least_index_sum = inf
        ans = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if i+j > least_index_sum:
                    break
                if list1[i] == list2[j]:
                    if i+j < least_index_sum:
                        ans = [list1[i]]
                        least_index_sum = i+j
                    else:
                        ans.append(list1[i])
        return ans
                
        