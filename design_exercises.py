"""
Shuffle an array
The most naïve implementation is to use both the randint and permutations
library functions and randomly choose one permutation. Considering the 
test will run 10 K calls, I'm not even attempting implementing that.

A hacky way to shuffle is to choose a random number between 0 and len(nums)-1
and use that as a pivot, that is break nums at pivot and swap left with right.
That fails test 5 probably because this strategy doesn't shuffle enough.

For the final version I realised that the permutations function yields an
iterator, so I didn't need stressing out.

"""
from itertools import permutations

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.permutations = permutations(nums)
        

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        try:
            shuffle = next(self.permutations)
        except StopIteration:
            self.permutations = permutations(self.nums)
            shuffle = next(self.permutations)
        
        return shuffle
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

"""
MinStack

The first implementation looked too easy to be true, and inevitably I missed
updating the minimum value after popping the minimum.

class MinStack:

    def __init__(self):
        self.stack_list = []
        self.min = float("inf")
        

    def push(self, val: int) -> None:
        self.stack_list.append(val)
        if val < self.min: self.min = val
        
    def pop(self) -> None:
        self.stack_list.pop()
        
    def top(self) -> int:
        return self.stack_list[-1]
        
    def getMin(self) -> int:
        return self.min
        
So I added a named tuple to keep track of the current minumum at any one time.
all methods run in O(1)
        
"""
from collections import namedtuple
class MinStack:
    ValuePair = namedtuple("ValuePair", "value min")

    def __init__(self):
        self.stack_list = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        if val < self.min: self.min = val
        self.stack_list.append(MinStack.ValuePair(val, self.min))
        
        
    def pop(self) -> None:
        last = self.stack_list.pop()
        if len(self.stack_list) == 0:
            self.min = float("inf")
        elif last.min < self.stack_list[-1].min:
            self.min = self.stack_list[-1].min
        
    def top(self) -> int:
        return self.stack_list[-1].value
        
    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class AlternativeClassMinStack:
    # perform constant time 
    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        # push element onto the stack 
        self.stack.append(val)
    def pop(self) -> None:
        # remove element on the top of the stack 
        if len(self.stack) > 0:
            self.stack.pop()
    def top(self) -> int:
        # get the top element of the stack 
        if len(self.stack) > 0:
            return self.stack[-1]
    def getMin(self) -> int:
        # retrieve the minimum element in the stack 
        if len(self.stack) > 0:
            tmp_ls = sorted(self.stack)
            return tmp_ls[0]
