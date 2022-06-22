class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        unique = dict()
        for num in nums:
            if num in unique:
                # no. of pairs that could be made, equals no. of same element                   already passed
                total += unique[num]
                unique[num] += 1 
            
            else:
                unique[num] = 1
        
        return total
    
'''
could use same dictionary of values for each element then loop on dict 
with : pairs for element =  n - 1 * n / 2
'''