#https://leetcode.com/problems/palindrome-number/description/

#Personal Solution 5ms
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        str_x = str(x)
        temp = str_x[::-1]
        return temp == str_x
        
        
#Top Solution 0ms
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        

solution = Solution()
result = solution.isPalindrome(12321)
print(result)