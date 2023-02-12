class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for char in s:
            if len(queue) == 0:
                queue.append(char)
            else:
                if queue[len(queue)-1] == self.openingOf(char):
                    queue.pop()
                else:
                    queue.append(char)
        return len(queue) == 0
    
    def openingOf(self, char: str) -> str:
        if char == ")":
            return "("
        elif char == "}":
            return "{"
        elif char == "]":
            return "["
        return "!!INVALIDCHAR!!"


sol = Solution()
print(sol.isValid("{}"))
print(sol.isValid("(){}[]"))
print(sol.isValid("(["))