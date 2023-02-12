class Solution:
    def romanToInt(self, s: str) -> int:
        special = ["I", "X", "C"];
        val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        total = 0
        index = 0
        while index < len(s):
            if s[index] in special and index != len(s)-1 and (s[index] + s[index+1] in val):
                total += val[s[index] + s[index+1]]
                index += 2
            else:
                total += val[s[index]]
                index += 1
        return total

sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))
print(sol.romanToInt("MCDLXXVI"))