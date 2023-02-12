from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        combo = []
        for digit in digits:
            combo.append(mapping[digit])
        combo.reverse()
        return self.appendLetters(combo, [])
    
    def appendLetters(self, letters: List[str], combo: List[str]) -> List[str]:
        if len(letters) > 0:
            curLetters = letters.pop()
            newCombo = []
            if len(combo) != 0:
                for group in combo:
                    for curLetter in curLetters:
                        newCombo.append(group + curLetter)
            else:
                for curLetter in curLetters:
                    newCombo.append(curLetter)
                
            return self.appendLetters(letters, newCombo)
        else:
            return combo
                
            
sol = Solution()
print(sol.letterCombinations("23"))