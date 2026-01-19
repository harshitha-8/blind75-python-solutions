"""
LeetCode #53: Maximum Subarray
Difficulty: Medium
Category: Array, Dynamic Programming, Divide and Conquer

Problem:
Given an integer array nums, find the contiguous subarray with the largest sum
and return its sum.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find maximum subarray sum using Kadane's Algorithm.
        
        Time Complexity: O(n) - single pass
        Space Complexity: O(1) - constant space
        
        Args:
            nums: List of integers
            
        Returns:
            Maximum sum of contiguous subarray
            
        Example:
            >>> Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
            6
        """
        # Kadane's Algorithm
        max_sum = nums[0]  # Global maximum
        current_sum = nums[0]  # Current subarray sum
        
        for num in nums[1:]:
            # Either extend current subarray or start new one
            current_sum = max(num, current_sum + num)
            
            # Update global maximum
            max_sum = max(max_sum, current_sum)
        
        return max_sum


class SolutionDP:
    """Dynamic Programming approach - more explicit"""
    
    def maxSubArray(self, nums: List[int]) -> int:
        """
        DP approach where dp[i] = max sum ending at index i.
        
        Time Complexity: O(n)
        Space Complexity: O(n) - dp array
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            # Either extend previous or start fresh
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        
        return max(dp)


class SolutionDivideConquer:
    """Divide and Conquer approach - O(n log n)"""
    
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Divide and conquer approach.
        
        Time Complexity: O(n log n)
        Space Complexity: O(log n) - recursion stack
        """
        def maxSubArrayHelper(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            
            # Max in left half
            left_max = maxSubArrayHelper(left, mid)
            
            # Max in right half
            right_max = maxSubArrayHelper(mid + 1, right)
            
            # Max crossing the middle
            left_sum = float('-inf')
            current_sum = 0
            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)
            
            right_sum = float('-inf')
            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)
            
            cross_sum = left_sum + right_sum
            
            return max(left_max, right_max, cross_sum)
        
        return maxSubArrayHelper(0, len(nums) - 1)


class SolutionBruteForce:
    """Brute force O(n²) - for educational purposes"""
    
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Check all possible subarrays.
        
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        max_sum = float('-inf')
        n = len(nums)
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)
        
        return max_sum


# For direct testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(solution.maxSubArray([1]))                               # 1
    print(solution.maxSubArray([5, 4, -1, 7, 8]))                 # 23
