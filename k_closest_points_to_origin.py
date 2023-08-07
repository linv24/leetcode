class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # list of tuples containing the point and its distance from the origin
        distances = [(pt, (pt[0]**2 + pt[1]**2)**(1/2)) for pt in points]
        distances = sorted(distances, key=lambda t: t[1])
        return [tup[0] for tup in distances[:k]]
