class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ### attempt 2
        # one ptr tracking the start of substring, dict mapping char
        # to most recent index. if repeat encountered (s[ptr] in dict), 
        # move start ptr to index after index found in dict
        # update dict at each step
        start = 0
        max_length = 0
        used = {}
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
        return max_length

        # ### attempt 1
        # # sliding window: right ptr iterates through string, 
        # # left ptr track beginning of current nonrepeating substring
        # # if right encounters repeated char, increment left until
        # # left encounters previous char, or left = right
        # l = 0 
        # longest = 0
        # so_far = ''
        # for r in range(len(s)):
        #     c = s[r]
        #     if c in s[l:r]:
        #         while s[l] != c and l < r:
        #             l += 1
        #         if l < r: 
        #             l += 1
        #     else:
        #         longest = max(longest, r - l + 1)
        #         print(longest, l, r)
        # return longestclass Solution(object):
