"""
LeetCode #217: Contains Duplicate
Difficulty: Easy
Category: Array, Hash Set

Problem:
Given an integer array nums, return true if any value appears at least twice,
and return false if every element is distinct.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check for duplicates using set length comparison.
        Most Pythonic approach.
        
        Time Complexity: O(n) - creating set
        Space Complexity: O(n) - set stores unique elements
        
        Args:
            nums: List of integers
            
        Returns:
            True if duplicates exist, False otherwise
            
        Example:
            >>> Solution().containsDuplicate([1, 2, 3, 1])
            True
        """
        return len(nums) != len(set(nums))


class SolutionIterative:
    """Iterative approach with early termination"""
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check for duplicates using iterative hash set.
        Best for early duplicate detection.
        
        Time Complexity: O(n) - worst case, can terminate early
        Space Complexity: O(n) - hash set
        """
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False


class SolutionSorting:
    """Sorting approach - space constrained environments"""
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check for duplicates using sorting.
        Best when space is constrained.
        
        Time Complexity: O(n log n) - sorting
        Space Complexity: O(1) - if sorting in-place allowed
        """
        nums.sort()
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        
        return False


class SolutionBruteForce:
    """Brute force O(n²) - not recommended"""
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check all pairs using nested loops.
        
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False


# For direct testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.containsDuplicate([1, 2, 3, 1]))           # True
    print(solution.containsDuplicate([1, 2, 3, 4]))           # False
    print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
