class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        
        alice_vals = set(aliceSizes)
        
        for size in set(bobSizes):
            target = (sum_alice - sum_bob) / 2 + (size)
            if target in alice_vals:
                return [target, size]


    