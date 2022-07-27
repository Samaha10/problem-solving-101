class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        guide = dict()
        total = 0
        
        for lett in chars:
            guide[lett] = 1 + guide.get(lett, 0)
        
        
        for word in words:
            w_count = dict()
            
            for lett in word:
                w_count[lett] = 1 + w_count.get(lett, 0)
            
            
            for l in w_count:
                if w_count[l] > guide.get(l, 0):
                    break
            else:
                total += len(word)
            
    
        return total
