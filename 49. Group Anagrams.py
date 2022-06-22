class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashgroup = collections.defaultdict(list)
        
        for word in strs:
            freq = dict()
            
            for letter in word:
                freq[letter] = 1 + freq.get(letter, 0)
            
            # tuple(sorted(freq.items()))
            hashgroup[frozenset(freq.items())].append(word)
        
        return hashgroup.values()