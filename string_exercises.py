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