class Solution:
    def isValid(self, s: str) -> bool:
        # case ((( or )))
        # putting one single if instead of 2 saved memory
        #if(all([brac in ['{', '(', '['] for brac in s]) or all([brac in ['}', ')', ']'] for brac in s])):
            #return False
        
        
        opening = []
        
        for brac in s:
            if brac in ['{', '(', '[']:
                opening.append(brac)
            
            else:
                # case more close brac than open[]]]], ()}
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
        
        # case ([]){ , check if open brac list is empty
        if not opening:
            return True
        