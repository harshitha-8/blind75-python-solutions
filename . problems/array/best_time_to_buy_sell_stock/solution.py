"""
LeetCode #121: Best Time to Buy and Sell Stock
Difficulty: Easy
Category: Array, Dynamic Programming

Problem:
You are given an array prices where prices[i] is the price of a stock on day i.
Find the maximum profit from buying and selling once.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find maximum profit using single-pass tracking.
        
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(1) - only two variables
        
        Args:
            prices: List of stock prices by day
            
        Returns:
            Maximum profit possible
            
        Example:
            >>> Solution().maxProfit([7, 1, 5, 3, 6, 4])
            5
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update minimum price seen so far
            min_price = min(min_price, price)
            
            # Calculate profit if we sell today
            current_profit = price - min_price
            
            # Update maximum profit
            max_profit = max(max_profit, current_profit)
        
        return max_profit


class SolutionKadane:
    """Alternative using Kadane's algorithm perspective"""
    
    def maxProfit(self, prices: List[int]) -> int:
        """
        Convert to maximum subarray problem.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        current_profit = 0
        
        for i in range(1, len(prices)):
            # Daily price change
            price_change = prices[i] - prices[i - 1]
            
            # Either extend current streak or start new
            current_profit = max(0, current_profit + price_change)
            
            # Track maximum
            max_profit = max(max_profit, current_profit)
        
        return max_profit


class SolutionBruteForce:
    """Brute force O(n²) solution - for comparison only"""
    
    def maxProfit(self, prices: List[int]) -> int:
        """
        Check all possible buy-sell pairs.
        
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        max_profit = 0
        n = len(prices)
        
        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        
        return max_profit


# For direct testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(solution.maxProfit([7, 6, 4, 3, 1]))     # 0
    print(solution.maxProfit([1, 2, 3, 4, 5]))     # 4
