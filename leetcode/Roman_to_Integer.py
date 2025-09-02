#https://leetcode.com/problems/roman-to-integer/description/

#Personal Solution 3ms
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        numbers = {
            "I" : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        for i in range(len(s)):
            if i+1 < len(s) and numbers[s[i]] < numbers [s[i+1]]:
                total -= numbers[s[i]]
            else:
                total += numbers[s[i]]
                
        return total
            
#Top Solution 0ms
class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        total = 0
        prev = 0

        for cha in reversed(s):
            cur = val[cha]

            if cur < prev:
                total -= cur
            else:
                total += cur
                prev = cur
        return total
            
solution = Solution()
result = solution.romanToInt("MCMXCIV")
print(result)