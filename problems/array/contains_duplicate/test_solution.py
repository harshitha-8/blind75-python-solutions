"""
Unit tests for Contains Duplicate problem.
Run with: pytest test_solution.py -v
"""

import pytest
from solution import Solution, SolutionIterative, SolutionSorting


class TestContainsDuplicate:
    """Test cases for Contains Duplicate problem"""
    
    @pytest.fixture
    def solution(self):
        return Solution()
    
    def test_example_1(self, solution):
        """Test: [1,2,3,1] -> True"""
        assert solution.containsDuplicate([1, 2, 3, 1]) is True
    
    def test_example_2(self, solution):
        """Test: [1,2,3,4] -> False"""
        assert solution.containsDuplicate([1, 2, 3, 4]) is False
    
    def test_example_3(self, solution):
        """Test: [1,1,1,3,3,4,3,2,4,2] -> True"""
        assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    
    def test_two_elements_duplicate(self, solution):
        """Test minimum size with duplicate"""
        assert solution.containsDuplicate([1, 1]) is True
    
    def test_two_elements_unique(self, solution):
        """Test minimum size without duplicate"""
        assert solution.containsDuplicate([1, 2]) is False
    
    def test_all_same(self, solution):
        """Test all elements are the same"""
        assert solution.containsDuplicate([7, 7, 7, 7, 7]) is True
    
    def test_negative_numbers(self, solution):
        """Test with negative numbers"""
        assert solution.containsDuplicate([-1, -2, -3, -1]) is True
    
    def test_large_range(self, solution):
        """Test with large number range"""
        assert solution.containsDuplicate([1000000000, -1000000000, 1000000000]) is True
    
    def test_single_element(self, solution):
        """Test single element"""
        assert solution.containsDuplicate([1]) is False


class TestIterativeApproach:
    """Test iterative hash set approach"""
    
    @pytest.fixture
    def solution(self):
        return SolutionIterative()
    
    def test_early_termination(self, solution):
        """Test that it stops as soon as duplicate found"""
        # Duplicate at positions 0 and 1
        assert solution.containsDuplicate([5, 5, 10, 20, 30]) is True


class TestSortingApproach:
    """Test sorting approach"""
    
    @pytest.fixture
    def solution(self):
        return SolutionSorting()
    
    def test_basic(self, solution):
        assert solution.containsDuplicate([1, 2, 3, 1]) is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
