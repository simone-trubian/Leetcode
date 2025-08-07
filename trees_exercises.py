from collections import deque
# The algorithm explores the left branch first until it reaches a leaf then
# the right branch until it reaches a leaf. when that is done it returns 0
# and adds for to each layer.
def maxDepth(self, root: Optional[TreeNode]) -> int:
    node = root
    if node is None:
        return 0
    else:
        left_depth = self.maxDepth(node.left)
        right_depth = self.maxDepth(node.right)
        return max(left_depth, right_depth) + 1

def alternativeMaxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

class Solution:
    
    @staticmethod
    def is_valid(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return Solution.is_valid(node.left, min_val, node.val) and \
               Solution.is_valid(node.right, node.val, max_val)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return Solution.is_valid(root, float("-inf"), float("inf"))
    
class Solution:
    @staticmethod
    def same(node1, node2):
        if not node1 and not node2:
            return True
        
        if not node1 or not node2:
            return False
        
        if node1.val != node2.val:
            return False
        
        return Solution.same(node1.left, node2.right) and \
               Solution.same(node1.right, node2.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return Solution.same(root, root)
        

# This exercise requires a breadth-first search
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        values = []
        
        while queue:
            level = []
            depth = len(queue)
            for _ in range(depth):
                node = queue.popleft()
                level.append(node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            values.append(level)
            
        return values

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(left, right):
            if left > right: return None
        
            m = (left+right) // 2
            root = TreeNode(nums[m])
            root.left = helper(left, m-1)
            root.right = helper(m+1, right)
            return root
        
        return helper(0, len(nums)-1)