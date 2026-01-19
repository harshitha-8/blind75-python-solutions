"""
LeetCode #238: Product of Array Except Self
Difficulty: Medium
Category: Array, Prefix Sum

Problem:
Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all elements of nums except nums[i].
You must solve it in O(n) time without using division.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate product except self using prefix and suffix products.
        
        Time Complexity: O(n) - three passes through array
        Space Complexity: O(1) - output array doesn't count as extra space
        
        Args:
            nums: List of integers
            
        Returns:
            List where answer[i] = product of all elements except nums[i]
            
        Example:
            >>> Solution().productExceptSelf([1, 2, 3, 4])
            [24, 12, 8, 6]
        """
        n = len(nums)
        answer = [1] * n
        
        # Step 1: Build prefix products in answer array
        # answer[i] = product of all elements to the left of i
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Step 2: Build suffix products and multiply with prefix
        # Multiply answer[i] by product of all elements to the right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer


class SolutionWithExtraSpace:
    """Alternative using separate prefix/suffix arrays (easier to understand)"""
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Use separate arrays for prefix and suffix products.
        
        Time Complexity: O(n)
        Space Complexity: O(n) - extra arrays
        """
        n = len(nums)
        
        # Build prefix products
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # Build suffix products
        suffix = [1] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # Combine prefix and suffix
        answer = [prefix[i] * suffix[i] for i in range(n)]
        
        return answer


class SolutionWithDivision:
    """Using division - violates problem constraints but educational"""
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculate using division (NOT ALLOWED per problem statement).
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Note: Doesn't handle zeros correctly without special cases
        """
        # Calculate total product
        total_product = 1
        zero_count = 0
        zero_index = -1
        
        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                zero_index = i
            else:
                total_product *= num
        
        # Handle edge cases with zeros
        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            result = [0] * len(nums)
            result[zero_index] = total_product
            return result
        else:
            return [total_product // num for num in nums]


# For direct testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.productExceptSelf([1, 2, 3, 4]))      # [24, 12, 8, 6]
    print(solution.productExceptSelf([-1, 1, 0, -3, 3])) # [0, 0, 9, 0, 0]
