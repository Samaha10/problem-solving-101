class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t = s[::]
        
        for i in range(len(s)):
            t = t[ :indices[i]] + s[i] + t[indices[i]+1: ]
            
                
        
        return t
    