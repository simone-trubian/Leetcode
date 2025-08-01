def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k%len(nums)
        swap_right = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = swap_right

def containsDuplicate(self, nums: List[int]) -> bool:
        #for i in range(len(nums)):
        #    for j in range(i+1, len(nums)):
        #        if nums[i] == nums[j]:
        #            return True
        #        
        #return False
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False

def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
            
        return nums[-1]

def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res =[]
        for value in nums1:
            for index in range(len(nums2)):
                if value == nums2[index]:
                    res.append(value)
                    nums2.pop(index)
                    break
        
        return res

def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(list(map(str,digits))))
        number += 1
        return list(map(int, list(str(number))))

def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeroes = 0
        while i<len(nums)-zeroes:
            if nums[i] == 0: 
                nums.pop(i)
                nums.append(0)
                zeroes += 1
            else:
                i += 1

def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
                
def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        side_len = len(matrix)
        
        for _ in range(side_len):
            matrix.append([x.pop(0) for x in reversed(matrix[:side_len])])
            
        for _ in range(side_len):
            matrix.pop(0)