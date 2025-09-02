#https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target):
        num_indices = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_indices:
                return [num_indices[complement], i]

            num_indices[num] = i

##Use the class
solution = Solution()
result = solution.twoSum([3,2,4], 6)
print(result)  # Output: [1, 2]
