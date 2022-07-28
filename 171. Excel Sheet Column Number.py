class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        power = 0
        num = 0
        
        for lett in reversed(columnTitle):
            place = ord(lett) - ord('A') + 1
            num += place * 26**power
            power += 1
        
        return num
            
            
        