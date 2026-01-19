"""
Unit tests for Product of Array Except Self problem.
Run with: pytest test_solution.py -v
"""

import pytest
from solution import Solution, SolutionWithExtraSpace


class TestProductExceptSelf:
    """Test cases for Product of Array Except Self"""
    
    @pytest.fixture
    def solution(self):
        return Solution()
    
    def test_example_1(self, solution):
        """Test: [1,2,3,4] -> [24,12,8,6]"""
        assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    
    def test_example_2(self, solution):
        """Test: [-1,1,0,-3,3] -> [0,0,9,0,0]"""
        assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    
    def test_two_elements(self, solution):
        """Test minimum size array"""
        assert solution.productExceptSelf([1, 2]) == [2, 1]
    
    def test_all_ones(self, solution):
        """Test array of all 1s"""
        assert solution.productExceptSelf([1, 1, 1, 1]) == [1, 1, 1, 1]
    
    def test_with_negatives(self, solution):
        """Test with negative numbers"""
        assert solution.productExceptSelf([-1, -2, -3]) == [6, 3, 2]
    
    def test_single_zero(self, solution):
        """Test with single zero"""
        assert solution.productExceptSelf([0, 1, 2, 3]) == [6, 0, 0, 0]
    
    def test_multiple_zeros(self, solution):
        """Test with multiple zeros"""
        assert solution.productExceptSelf([0, 0, 1, 2]) == [0, 0, 0, 0]
    
    def test_large_numbers(self, solution):
        """Test with larger numbers"""
        assert solution.productExceptSelf([2, 3, 4, 5]) == [60, 40, 30, 24]


class TestExtraSpaceApproach:
    """Test solution with extra space"""
    
    @pytest.fixture
    def solution(self):
        return SolutionWithExtraSpace()
    
    def test_basic(self, solution):
        assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
