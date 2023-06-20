class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        T = [0] * (n+1)
        T[1] = 1
        T[2] = 2
        for i in range(3,n+1):
            T[i] = T[i-1] + T[i-2]
        return T[n]
