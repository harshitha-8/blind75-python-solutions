"""
Unit tests for Maximum Subarray problem.
Run with: pytest test_solution.py -v
"""

import pytest
from solution import Solution, SolutionDP, SolutionDivideConquer


class TestMaxSubArray:
    """Test cases for Maximum Subarray"""
    
    @pytest.fixture
    def solution(self):
        return Solution()
    
    def test_example_1(self, solution):
        """Test: [-2,1,-3,4,-1,2,1,-5,4] -> 6 ([4,-1,2,1])"""
        assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    
    def test_example_2(self, solution):
        """Test: [1] -> 1"""
        assert solution.maxSubArray([1]) == 1
    
    def test_example_3(self, solution):
        """Test: [5,4,-1,7,8] -> 23"""
        assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23
    
    def test_all_negative(self, solution):
        """Test all negative numbers"""
        assert solution.maxSubArray([-3, -2, -5, -1]) == -1
    
    def test_all_positive(self, solution):
        """Test all positive numbers"""
        assert solution.maxSubArray([1, 2, 3, 4, 5]) == 15
    
    def test_alternating(self, solution):
        """Test alternating positive/negative"""
        assert solution.maxSubArray([1, -1, 1, -1, 1]) == 1
    
    def test_single_negative(self, solution):
        """Test single negative number"""
        assert solution.maxSubArray([-1]) == -1
    
    def test_zeros(self, solution):
        """Test with zeros"""
        assert solution.maxSubArray([0, -1, 0, -1, 0]) == 0


class TestDPApproach:
    """Test DP solution"""
    
    @pytest.fixture
    def solution(self):
        return SolutionDP()
    
    def test_basic(self, solution):
        assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


class TestDivideConquer:
    """Test divide and conquer approach"""
    
    @pytest.fixture
    def solution(self):
        return SolutionDivideConquer()
    
    def test_basic(self, solution):
        assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
