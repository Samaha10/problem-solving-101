class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        abs_max = 0
        ordered = sorted(set(nums))
        counter = 0
        
        for i in range(0, len(ordered) - 1):
            if ordered[i + 1] - ordered[i] == 1:
                counter += 1
            else:
                counter = 0
            abs_max = max(abs_max, counter)
        
        return abs_max + 1
                
            