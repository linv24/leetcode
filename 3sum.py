class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # try two sum solution, but modifying target to be each entry in nums
        # triplets = set()
        # for i, n in enumerate(nums):
        #     diffs = set()
        #     for j, m in enumerate(nums[i+1:]):
        #         if m in diffs:
        #             triplets.add(tuple(sorted([n, m, -n - m])))
        #         else:
        #             diffs.add(-n - m)
        # return [list(t) for t in triplets]

        # first, sort list
        # continue with three pointers: left, mid, right
            # at each iteration, test whether left, mid, and right nums add to 0
            # increment either mid, right, or both to avoid duplicates (easy bc list is sorted)
            # increment mid and decrement right if sum found 
        nums.sort()
        triplets = []
        for left in range(len(nums) - 2):
            if left > 0 and nums[left-1] == nums[left]:
                continue
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]
                if curr_sum < 0: # sum too low, increment mid to increase sum
                    mid += 1
                elif curr_sum > 0: # sum too high, decrement right to decrease sum
                    right -= 1
                else: # sum just right
                    triplets.append([nums[left], nums[mid], nums[right]])
                    # check for duplicates
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right-1]:
                        right -= 1
                    mid += 1
                    right -= 1
        return triplets
