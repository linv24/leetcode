class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert to set, check if n-1 or n+1 in set for each n in nums
        nums = set(nums)
        # To avoid checking sequences multiple times, only start from
        # initial elt in each sequence, ie. only check if n-1 not in set
        max_len = 0
        for n in nums:
            if n - 1 not in nums:
                m = n + 1
                while m in nums:
                    m += 1
                max_len = max(m - n, max_len)
        return max_len
