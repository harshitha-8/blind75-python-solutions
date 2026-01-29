from typing import List
import unittest

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to 
        the product of all the elements of nums except nums[i].
        
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        
        You must write an algorithm that runs in O(n) time and without using the division operation.
        """
        n = len(nums)
        res = [1] * n

        # Pass 1: Calculate Prefix products
        # Store the product of all elements to the left of i in res[i]
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Pass 2: Calculate Postfix products
        # Multiply the stored prefix product by the product of all elements to the right
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

# Unit Tests to verify the solution
class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertEqual(self.solution.productExceptSelf(nums), expected)

    def test_example_2(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertEqual(self.solution.productExceptSelf(nums), expected)

if __name__ == '__main__':
    unittest.main()
