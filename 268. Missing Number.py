class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # if 0 not in nums return 0
        passed = [-1] * (len(nums) + 1)
        
        for elem in nums:
            passed[elem] = 1
        
        for i, elem in enumerate(passed):
            if elem == -1:
                return i
        
        # complete sequence then last + 1
        return len(passed)
