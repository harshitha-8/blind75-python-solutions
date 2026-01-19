"""
LeetCode #1: Two Sum
Difficulty: Easy
Category: Array, Hash Map

Problem:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers that add up to target using hash map.
        
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(n) - hash map stores up to n elements
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices [index1, index2]
            
        Example:
            >>> Solution().twoSum([2, 7, 11, 15], 9)
            [0, 1]
        """
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        
        return []  # No solution found (won't happen per problem constraints)


class SolutionBruteForce:
    """Alternative O(n²) brute force solution - not recommended"""
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force approach using nested loops.
        
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# For direct testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(solution.twoSum([3, 2, 4], 6))       # [1, 2]
    print(solution.twoSum([3, 3], 6))          # [0, 1]
