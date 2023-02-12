from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPre = ""
        index = 0
        while index >= 0:
            curLetter = ""
            for str in strs:
                if curLetter == "":
                    curLetter = str[index]
                else:
                    if curLetter != str[index]:
                        return longestPre
            longestPre += curLetter
            index += 1
        return longestPre

            
            
sol = Solution()

print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))