class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for c in magazine:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for c in ransomNote:
            if c not in d or d[c] == 0:
                return False
            else:
                d[c] -= 1
        return True
