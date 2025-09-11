def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        half_len = len(s)//2
        
        for idx, char in enumerate(s[:half_len]):
            last_char = s[-(1+idx)]
            s[-(1+idx)] = char
            s[idx] = last_char

def reverse(self, x: int) -> int:
        
        is_negative = x<0
        string_x = str(abs(x))
        list_x = list(string_x)
        reversed_string = "".join(reversed(list_x))
        reversed_int = int(reversed_string)
        if reversed_int<-2**31 or reversed_int>2**31 - 1:
            return 0
        if is_negative:
            return -reversed_int
        
        return reversed_int

def firstUniqChar(self, s: str) -> int:
        seen = set()
        for idx, letter in enumerate(s):
            if letter in seen:
                continue
            if letter not in s[idx+1:]:
                return idx
            seen.add(letter)
        return -1

def alternativeFirstUniqChar(self, s: str) -> int:
        hashmap={}
        for c in s :
            hashmap[c]=1+hashmap.get(c,0)
        for i,c in enumerate(s):
            if hashmap[c]==1:
                return i
        return -1

def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = dict()
        for letter in s:
            s_dict[letter] = 1+s_dict.get(letter,0)
            
        t_dict = dict()
        for letter in t:
            t_dict[letter] = 1+t_dict.get(letter,0)
            
        for letter in s_dict.keys():
            if s_dict.get(letter) != t_dict.get(letter, 0):
                return False
        
        return True

def alternativeIsAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}

        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True


def isPalindrome(self, s: str) -> bool:
        stripped_s = "".join([x.casefold() for x in s if x.isalnum()])
        
        for idx in range(len(stripped_s)//2):
            if stripped_s[idx] != stripped_s[(len(stripped_s)-(1+idx))]:
                return False
        
        return True

def alternativeIsPalindrome(self, s: str) -> bool:
        
        cleanS="".join(filter(str.isalnum, s)).lower()
        left=0
        right=len(cleanS)-1
        while left < right:
            if cleanS[left] != cleanS[right]:
                return False

            left +=1
            right -=1
        return True

def find_prefix(s1: str, s2: str) -> int:
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    
    return i
    
def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) < 2:
        return strs[0]
    
    i = 1
    prefix = find_prefix(strs[i-1], strs[i])
    
    if prefix == -1:
        return ""
    
    for i in range(1, len(strs)):
        if strs[i-1][:prefix] != strs[i][:prefix]:
            prefix = find_prefix(strs[i-1], strs[i])
            if prefix == -1:
                return ""
         
    
    return strs[i][:prefix]

def alternativeLongestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]
        for i in range(1,len(strs)):
            current = strs[i]
            temp = longest_prefix
            longest_prefix = ""
            for j in range(len(current)):
                if j < len(temp) and current[j] == temp[j]:
                    longest_prefix += temp[j]
                else:
                    break

        return longest_prefix

"""
Leetcode 75 Merge strings alternatively
1. Check which one is the shortest word and use its length as upper bound for a cycle
    you can reassign word1 and word2 to long and short
2. iterate with range using the shortest length
3. in the loop create a result string by concatenating the character at that index in both strings
4. When the cycle finishes append the remaining characters of the long string

Runs in O(n) complexity and O(n) space?
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) <= len(word2):
            short_s = word1
            long_s = word2
        else:
            short_s = word2
            long_s = word1

        result = ""
        for i in range(len(short_s)):
            result = result + word1[i] + word2[i]
        
        return result + long_s[len(short_s):]

"""
Leetcode 1071. Greatest Common Divisor of Strings
First one could try dividing a string with the other using the "in" operator
but that doesn't give you the common denominator
Another option is to use sets and do an itersection of the sets.
1. Create a set with all the characters of str1
2. Create a set with all the characters of str2
3. Intersect the sets
4. Return the intersection
Complexity O()
Space O()

While this strategy works and doesn't violate the problem as stated it's
not an accepted answer. Another strategy is to pick one string and build a substring one character at a time starting from the leftmost character, then testing if that substring is present in the other string.

Of course, I haven't thought about this well enough since this algo is too greedy.

What if I scan one string extracting a character at a time and check if that character is in the other string as well? if so concatenate it to the result string. This is still too greedy.

|
ABCDEF
|
ABC

ABABAB

ABAB

ABAABA

ABA

cases:
    1. The strings have the same length: check if they are the same
    2. One string is smaller: there has to be a substring that is present in both strings and the string has to be a multiple of the substring
    3.

- scan the shotest string one character at a time
- check if the character is also present at the same index in the longest string
    if not return false
- 

- find if the shortest string is included in the largest string
- find if the shortest string is repeated in the largest string
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Attempt 1
        set1 = set(list(str1))
        set2 = set(list(str2))
        if set1 == set2:
            return str1[:len(set1)]
        else:
            return ""
        """
        Attempt 2
        i = 0
        len1 = len(str1)
        len2 = len(str2)
        result = ""
        while i <= len1 and i <= len2 and (str1[:i] in str2):
            i += 1
        return str1[:i]
        """

"""
392. Is Subsequence

For this exercise one cannot use a set because order must be preserved, at least this time we know s must be a sub-sequence of t

A way to do it is to brute-force every char of s and find it in t, as long as you preserve the last index you searched t at, it can be done in linear time

let it be
i the index of t
j the index of s
j = i = 0
- enumerate over t
- check if s[j] == t[i]
    if so increment j
at the end of the loop find out if j == len(s)

I decided to change the loop in a while to avoid the IndexError
Complexity O(n)
Space O(1)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = j = 0

        while j < len(s) and i < len(t):
            if s[j] == t[i]: j += 1
            i += 1

        return j == len(s)