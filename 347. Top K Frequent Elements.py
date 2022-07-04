class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()
        for elem in nums:
            frequency[elem] = 1 + frequency.get(elem, 0)
        #  operator.itemgetter(1)
        desc_freq = sorted(frequency.items(), key = lambda item:item[1], 
        reverse  =True)
        return [s[0] for s in desc_freq[:k]]