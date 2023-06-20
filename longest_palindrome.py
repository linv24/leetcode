class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        # count characters
        for c in s:
            if c in d:
                d[c] += 1
            else: 
                d[c] = 1
        total = 0
        odd_picked = False
        for c in d:
            # if count is even, add all letters to palindrome
            if d[c]%2 == 0:
                total += d[c]
            # if count is the first odd one, add all letters
            elif not odd_picked:
                odd_picked = True
                total += d[c]
            # if count is not the first odd one, remove one and add remaining letters
            else:
                total += d[c] - 1
        return total
