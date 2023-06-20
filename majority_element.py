class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count helps track the majority elt so far. Only the most frequent elt
        # so far is tracked, and the most frequent changes only when the count
        # decrements to 0. Since the majority element n contains the most elts,
        # with at least (n/2 + 1) elts (incrementing count) and at most (n/2 - 1)
        # non-elts (decrementing count), the count is guaranteed to return the
        # majority elt
        count = 0
        best = None
        for n in nums:
            if n == best:
                count += 1
            else:
                if count > 0:
                    count -= 1
                else: 
                    best = n
        return best
