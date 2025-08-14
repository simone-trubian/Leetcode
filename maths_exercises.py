class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                res.append("FizzBuzz")
            elif i%3 == 0:
                res.append("Fizz")
            elif i%5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))

        return res
    
    """
Prime numbers < n

I attempted coming up with a solution myself, but I was more interested in learning
a clever mathematical trick to work out systematically prime numbers; in my research
I encountered the Eratostene's sieve.
The algorithm initialises the "sieve" -a list that marks as True a number if prime- as
all True. Then starting from two (which is prime) the algorithm marks as false all multiples,
thus exluding them from prime number list.

This algorithm isn't optimised since it calculates all even numbers and it doesn't stop at
sqrt of p.
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        primes_total = 0
        sieve = [True for _ in range(n)]
        for p in range(2, n):
            if (sieve[p]):
                primes_total += 1
                for i in range(p, n, p):
                    sieve[i] = False
        
        return primes_total
        
"""
Power of Three

Runs in O(n) complexity and O(1) space
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n == 1: return True
        n = float(n)
        
        while n != 3 and n > 3 and n.is_integer():
            n = n / 3
            
        return n == 3
    
"""
Roman numerals to int
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
    
        for i in range(len(s)):
            if i > 0 and roman_dict[s[i]] > roman_dict[s[i-1]]:
                result += roman_dict[s[i]] - 2 * roman_dict[s[i-1]]
            else:
                result += roman_dict[s[i]]
        
        return result