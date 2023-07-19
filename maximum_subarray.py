class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # T[0][i] keeps track of the max subarray including ix i
        # T[1][i] keeps track of the max subarray with OR without i
        T = [[0] * len(nums) for _ in range(2)]
        # base case
        T[0][0], T[1][0] = nums[0], nums[0]
        # bottom up dp
        for i in range(1, len(nums)):
            # max of ix i or ix i + subarray before
            T[0][i] = max(nums[i], nums[i] + T[0][i-1])
            # max of subarray before or ix i + subarray before
            T[1][i] = max(T[1][i-1], T[0][i])
        return max(T[0][-1], T[1][-1])
