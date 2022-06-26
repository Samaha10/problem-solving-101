class Solution:
    def isValid(self, s: str) -> bool:        
        opening = []
        
        for brac in s:
            if brac in ['{', '(', '[']:
                opening.append(brac)
            
            else:
                if not opening:
                    return False
                
                last_open = opening.pop()
                
                if brac == ')':
                    if last_open == '(':
                        continue
                    else:
                        return False
                
                if brac == ']':
                    if last_open == '[':
                        continue
                    else:
                        return False
                
                if brac == '}':
                    if last_open == '{':
                        continue
                    else:
                        return False
        
        if not opening:
            return True
        
