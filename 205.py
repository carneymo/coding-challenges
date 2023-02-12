class Solution:
    def isomorphic(self, s: str, t: str):
        print(self.isIsomorphic(s,t))

    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for index in range(len(s)):
            if s[index] not in sMap and t[index] not in tMap:
                sMap[s[index]] = t[index]
                tMap[t[index]] = s[index]
            elif s[index] not in sMap and t[index] in tMap:
                return False
            elif t[index] not in tMap and s[index] in sMap:
                return False
            if sMap[s[index]] != t[index]:
                return False
            if tMap[t[index]] != s[index]:
                return False
        return True

sol = Solution()
sol.isomorphic("egg", "add")
sol.isomorphic("foo", "bar")
sol.isomorphic("paper", "title")
sol.isomorphic("badc", "baba")
sol.isomorphic("egcd", "adfd")