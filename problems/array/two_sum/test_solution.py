"""
Unit tests for Two Sum problem.
Run with: pytest test_solution.py -v
"""

import pytest
from solution import Solution, SolutionBruteForce


class TestTwoSum:
    """Test cases for Two Sum problem"""
    
    @pytest.fixture
    def solution(self):
        """Create solution instance for testing"""
        return Solution()
    
    def test_example_1(self, solution):
        """Test case: [2,7,11,15], target=9"""
        assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    
    def test_example_2(self, solution):
        """Test case: [3,2,4], target=6"""
        assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    
    def test_example_3(self, solution):
        """Test case: [3,3], target=6"""
        assert solution.twoSum([3, 3], 6) == [0, 1]
    
    def test_negative_numbers(self, solution):
        """Test with negative numbers"""
        assert solution.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
    
    def test_with_zero(self, solution):
        """Test with zero in array"""
        assert solution.twoSum([0, 4, 3, 0], 0) == [0, 3]
    
    def test_negative_target(self, solution):
        """Test with negative target"""
        assert solution.twoSum([-3, 4, 3, 90], 0) == [0, 2]
    
    def test_large_numbers(self, solution):
        """Test with large numbers"""
        assert solution.twoSum([1000000000, 999999999, 1], 1999999999) == [0, 1]
    
    def test_two_elements(self, solution):
        """Test minimum size array"""
        assert solution.twoSum([1, 2], 3) == [0, 1]


class TestTwoSumBruteForce:
    """Test brute force solution"""
    
    @pytest.fixture
    def solution(self):
        return SolutionBruteForce()
    
    def test_basic(self, solution):
        assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
