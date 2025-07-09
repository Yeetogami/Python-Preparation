class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):
            for j in range(1, (len(nums))):
                if nums[i]+nums[j] == target and i != j:
                    l.append(i)
                    l.append(j)
                    return l
                j = j+1
            i = i+1
            
        