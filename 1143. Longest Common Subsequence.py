class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        x = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                if text1[i] == text2[j]:
                    x[i][j] = 1 + x[i+1][j+1]
                
                else:
                    x[i][j] = max(x[i][j+1], x[i+1][j])
            
        return x[0][0]
                    
        