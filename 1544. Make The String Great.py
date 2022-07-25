class Solution:
    def makeGood(self, s: str) -> str:
        valids = []
        
        for letter in s:
            if valids:
                if abs(ord(valids[-1]) - ord(letter)) == 32:
                    del valids[-1]
                    continue
                
            valids.append(letter)
        
        return "".join(valids)
            
        