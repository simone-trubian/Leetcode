"""
The naïve implementation is:
1 - Chop nums1 at m
2 - Extend nums1 with nums2
3 - Call the 'sorted' function and assign the results to nums1
nums1 = nums1[:m]
nums1.extend(nums2)
nums1 = sorted(nums1)
This solution works in python but not in Leetcode, probably because the assignments loose the reference to the original list.

A less naïve solution is to:
1 - Overwrite the zeros in nums1 with the values in nums2 using a cycle traversing the whole of nums2
2 - Sort with an in-place algorithm (such as insert sort) nums1, now containing all values

The complexity is of O(n) for the first part plus a O(n^2) for the sorting, making it a O(n^2)
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i, n in enumerate(nums2):
            nums1[m+i] = n
            
        for i in range(1, len(nums1)):
            key_item = nums1[i]
            j = i - 1
            
            while j >= 0 and nums1[j] > key_item:
                nums1[j + 1] = nums1[j]
                j -= 1
                
            nums1[j + 1] = key_item

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
"""
First Bad Version Problem

Naïve implementation
- Scan all numbers from 1 to n until we hit the first False reply
- Break loop and return current index

def firstBadVersion(self, n: int) -> int:
        for index in range(1, n+1):
            if isBadVersion(index): break
        
        return index
        
This wil run in O(n) and will hit the time limit
-------------------------------------------------

A more sophisticated approach will require a recursive search doing the following
- Find the midpoint
- Call fun to find if version is bad
    if good check the next version
        if bad return midpoint + 1
        else call recursively to the midpoint between the current midpoint and n
    else (version is bad) check the previous version
        if bad call recursively to the midpoint beteen the current midpoint and 1
        else (previous version is good) return the midpoint

@staticmethod
def find_version(n: int, midpoint: int) -> int:
        
    if isBadVersion(midpoint):
        # Midpoint version is bad
        if isBadVersion(midpoint-1):
            return Solution.find_version(n, midpoint//2)
        else:
            return midpoint
    else:
        # Midpoint version is good
        if isBadVersion(midpoint+1):
            return midpoint+1
        else:
            return Solution.find_version(n, n-(midpoint//2))
        
def firstBadVersion(self, n: int) -> int:
    return Solution.find_version(n, n//2)

This solution has complexity of O(log2 n) but being recrusive, it will hit the stack limit.
--------------------------------------------------------
The third solution is to change the algorithm into an iterative one. Annoyingly this also seem to hit the time limt. 


class Solution:
    
    @staticmethod
    def find_version(n: int, midpoint: int) -> int:
        while True:
            if isBadVersion(midpoint):
                # Midpoint version is bad
                if isBadVersion(midpoint-1):
                    midpoint = midpoint//2
                else:
                    return midpoint
            else:
                # Midpoint version is good
                if isBadVersion(midpoint+1):
                    return midpoint+1
                else:
                    midpoint = n-(midpoint//2)
        
    def firstBadVersion(self, n: int) -> int:
        return Solution.find_version(n, n//2)
            
-----------------------------------------------------------------------

The fourth solution optimises the third by tighening the bounds.
It introduces the concepts of upper and lower bounds created in the previous 
searches ensuring the search doesn't widen back to areas already explored.
Infuriatingly, even this optimised version hits the time limit. 

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower_bound = 1
        upper_bound = n
        midpoint = n//2
        
        while True:
            if isBadVersion(midpoint):
                # Midpoint version is bad
                if isBadVersion(midpoint-1):
                    upper_bound = midpoint
                    midpoint = upper_bound//2
                else:
                    return midpoint
            else:
                # Midpoint version is good
                if isBadVersion(midpoint+1):
                    return midpoint+1
                else:
                    lower_bound = midpoint
                    midpoint = upper_bound - (lower_bound//2)
   
-------------------------------------------------------------
The final solution is not from me. The loop goal is to tighen the search
space to the point the first bad version is identified. Unlike my previous
version is not trying to short-circuit the algorithm by expanding the search
one to the right or left of the midpoint. This algorithm is more efficient
because it minimises calls to the API.    
"""""
    
class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower_bound = 1
        upper_bound = n
        
        while lower_bound < upper_bound:
            midpoint = (lower_bound + upper_bound) // 2
            if isBadVersion(midpoint):
                upper_bound = midpoint
            else:
                lower_bound = midpoint + 1
        
        return lower_bound
    
""""
Climbing Stairs
When solving the problem on paper I realised the sequence is a Fibonacci series.
The following algorithm is and optimised imperative solution for Fibo. The only
caveat is that n needs to be incremented by one.

The algo runs in O(n) time and O(1) space.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
    
        prevPrev, prev, curr = 0, 1, 1
        n = n+1
        # Using the bottom-up approach
        for i in range(2, n + 1):
            curr = prev + prevPrev
            prevPrev = prev
            prev = curr

        return curr