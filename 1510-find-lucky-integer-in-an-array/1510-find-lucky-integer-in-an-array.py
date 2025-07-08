from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = []
        count = Counter(arr)
        for key, value in count.items():
            if key == value:
                lucky.append(key)
        if lucky:
            return max(lucky) 
        else:
            return -1