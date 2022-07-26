class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        
        while (left < right) and (left < len(s)):
            if s[left].lower() in "aeiou":
                while(left < right):
                    if s[right].lower() in "aeiou":
                        temp = s[left]
                        s = s[:left] + s[right] + s[left + 1:]
                        s = s[:right] + temp + s[right + 1:]
                        right -= 1
                        break
                    
                    right -= 1
            
            
            left += 1
        
        return s
        