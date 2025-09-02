#https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        first_shortest = min(strs, key=len)
        
        while first_shortest:
            if all(s.startswith(first_shortest) for s in strs):
                return first_shortest
            first_shortest = first_shortest[:-1]
            
        return ""
    
    
solution = Solution()
result = solution.longestCommonPrefix(["flower","flow","floght"])
print(result)