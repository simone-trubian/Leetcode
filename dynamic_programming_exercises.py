
""""
Climbing Stairs
When solving the problem on paper I realised the sequence is a Fibonacci series.
The following algorithm is and optimised imperative solution for Fibo. The only
caveat is that n needs to be incremented by one.

The algo runs in O(n) time and O(1) space.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
    
        prev_prev, prev, curr = 0, 1, 1
        n = n+1
        # Using the bottom-up approach
        for i in range(2, n + 1):
            curr = prev + prev_prev
            prev_prev = prev
            prev = curr

        return curr

"""
This problem requires searching the entire data structure, however it is
a given that the only acceptable maximum must be right of the minimum.

The naïve implementation is to traverse the array once to find the minimum
value, in case there is more than one the first minimum. Then traverse again
the array starting from the minimum to search the maximum value. This algo
runs in O(2n) which is why I'm not even bothering implementing it.

Another option is to do a single search memorising the current minimum and max
after the min, together with the profit. Every time a new local minimum is found,
min and max are reset to that local minimum and the profit memorised. Each time
a new local maximum is found, the current maximum and current profit are set.

This version runs in O(n)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = max_price = prices[0]
        current_profit = previous_profit = 0

        for i in range(len(prices)):
            # A new local minimum is found
            if prices[i] < min_price:
                if current_profit >= previous_profit:
                    previous_profit = current_profit
                current_profit = 0
                min_price = max_price = prices[i]
            # A new local maximum is found
            elif prices[i] > max_price:
                max_price = prices[i]
                current_profit = max_price - min_price
            
        return max(previous_profit, current_profit)
    
    
"""
Maximum Subarray

I can make a few assumptions:
1 - The sub-array has to be made of contiguous numbers
2 - The sub-array can be of length 1
3 - As long as the sum of the sub-array is > 0 it's worth keeping all
    elements, even negative ones.
    
This problem requires traversing the array fully once with at least one index.
The mistake I made was forgetting I only need the sum, not the indexes of the sub-array.

This is a greedy-like algorithm. It initalises the current_sum at zero since the array
hasn't been traversed yet, and the max sum at the lowest possible values since we migh
only get negative values in the array.

The algo then traverses the array, it updates the current sum regardless of whether
the next value is negative or positive, because it doesn't know what comes next. The
value of the max sum is kept updated and in case the current sum goes negative, it's
reset to zero.

This implementation runs in O(n) complexity an O(1) space
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)
            
            if current_sum < 0:
                current_sum = 0
                
        return max_sum
    
"""
House Robber
This problem requires traversing the array at least once. There can only be
two possible solutions: one is the sum of values in even indexes in the array
the other the sum of values in even indexes in the array. return the highes sum.
This is the greediest pattern, the one that optimises for capturing the highest
number of array elements, but doesn't work with this array [10, 1, 1, 10, 1, 1, 10]
where the highest sum is 30 which doesn't follow the odds or even pattern.

This is because the problem needs to be broken down in terms of top-down dynamic
programming. The problem can be solved by constantly finding the maximum running 
total between either the current value in the array plus the sum of the values up 
to n-2 or the sum of the values up to n-1.

This algorithm runs in O(n) complexity and O(1) space
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        minus_two = minus_one = 0
        
        # [minus_two, minus_one, n, n+1, ...]
        for n in nums:
            current_max = max(minus_two+n, minus_one)
            minus_two = minus_one
            minus_one = current_max
        
        return minus_one
        