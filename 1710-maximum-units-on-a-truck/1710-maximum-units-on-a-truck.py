class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        ret = 0
        for box in boxTypes: 
            ret += box[0]*box[1]
            truckSize -= box[0]
            if 0 >= truckSize:
                ret += box[1]*truckSize
                break
        return ret