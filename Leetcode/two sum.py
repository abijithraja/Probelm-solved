class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store the numbers and their indices
        num_map = {}
        
        # Iterate over the nums array
        for i, num in enumerate(nums):
            complement = target - num
            
            # If complement is already in the dictionary, we found the solution
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, store the current number and its index in the dictionary
            num_map[num] = i
        
        # If no solution is found (this shouldn't happen given the problem constraints)
        return []

# Example usage:
solution = Solution()
nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(solution.twoSum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(solution.twoSum(nums3, target3))  # Output: [0, 1]
