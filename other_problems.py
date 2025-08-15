"""
Hamming Weight

Extract all the bits from a number using bitwise operations.

Runs in O(n) where n is the number of bits in a number and O(1) space
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        weight = 0

        while n > 0:
            weight += int(n & 1)
            n >>= 1
        
        return weight
        
"""
Hamming distance

In practice is how many are different between two numbers.
The algorithm does a bit-wise and with 1 to find out if the
last bit of the number is a one or a zero. If they are different
the distance is incremented. The algorithm then shifts bitwise
until both numbers have all been reduced to zero.

"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        
        while x or y:
            if (x & 1) != (y & 1): distance += 1
            x >>= 1
            y >>= 1
        
        return distance
                
"""
Reverse bits

Probably the solution below is a hack.

Runs in O(1) complexity and O(1) space
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        return int("0b" + "".join(reversed('{0:032b}'.format(n))), 2)
    
"""
 Pascal's Triangle
 
 - Fetch previous row
 - Add a one
 - Traverse the previous row starting from index 1. Sum that value to i-1
 - Add onother one and complete the new row
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        elif numRows == 2: return [[1],[1,1]]
        
        triangle = [[1],[1,1]]
        i = 1
        # Build all rows
        while i < numRows-1:
            new_row = [1]
            previous_row = triangle[i]
            #Build single row
            for j in range(len(previous_row)-1):
                new_row.append(previous_row[j]+previous_row[j+1])
            new_row.append(1)
            triangle.append(new_row)
            i +=1
        
        return triangle
    
"""
Valid Parentheses

Balanced parenthes problems are best solved with the aid of a stack.
In this case the problem is slighly complicated by having more than
one type of parentheses and the expectation they should still be balanced.
The algo pushes to the stack for open par and pops for closed par, with
the extra step of comparing the popped par with the expected type using
a dictionary.

Runs in complexity O(n) and O(1) space
"""
class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")" or char == "]" or char == "}":
                try:
                    popped = stack.pop()
                    if popped != d[char]: return False
                except IndexError:
                    return False
        
        return stack == []
        
    
"""
Missing Number

Because of the constraints of the input the problem can be easily solved
by subtractig the result of (n*n+1)/2 to the sum of the values in the array
giving the missing number.

Runs in O(n) complexity and O(1) space
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return ((len(nums) * (len(nums)+1)) // 2) - sum(nums) 
    
    def alternativeMissingNumber(self, nums: List[int]) -> int:
        ans = float('-inf')
        n = len(nums)
        
        for i in range(0,n+1):
            if i not in nums:
                ans = i
                break
        return ans
            
        