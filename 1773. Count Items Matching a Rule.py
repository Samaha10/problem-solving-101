class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        indicies = {'color': 1, 'type': 0, 'name': 2}
        
        return sum(1 for item in items if item[indicies[ruleKey]] == ruleValue)
        