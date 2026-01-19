"""
Unit tests for Best Time to Buy and Sell Stock problem.
Run with: pytest test_solution.py -v
"""

import pytest
from solution import Solution, SolutionKadane, SolutionBruteForce


class TestMaxProfit:
    """Test cases for Best Time to Buy and Sell Stock"""
    
    @pytest.fixture
    def solution(self):
        return Solution()
    
    def test_example_1(self, solution):
        """Test: [7,1,5,3,6,4] -> 5"""
        assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    
    def test_example_2(self, solution):
        """Test: [7,6,4,3,1] -> 0 (decreasing prices)"""
        assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    
    def test_increasing_prices(self, solution):
        """Test strictly increasing prices"""
        assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
    
    def test_single_price(self, solution):
        """Test single element"""
        assert solution.maxProfit([5]) == 0
    
    def test_two_prices_profit(self, solution):
        """Test two prices with profit"""
        assert solution.maxProfit([1, 5]) == 4
    
    def test_two_prices_no_profit(self, solution):
        """Test two prices with no profit"""
        assert solution.maxProfit([5, 1]) == 0
    
    def test_all_same_prices(self, solution):
        """Test all same prices"""
        assert solution.maxProfit([5, 5, 5, 5]) == 0
    
    def test_multiple_peaks(self, solution):
        """Test multiple peaks and valleys"""
        assert solution.maxProfit([3, 2, 6, 5, 0, 3]) == 4
    
    def test_large_profit(self, solution):
        """Test large profit difference"""
        assert solution.maxProfit([1, 1000]) == 999


class TestKadaneApproach:
    """Test Kadane's algorithm approach"""
    
    @pytest.fixture
    def solution(self):
        return SolutionKadane()
    
    def test_basic(self, solution):
        assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
