class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = {}
        for point1, point2 in points:
            result = math.sqrt((0 - point1) ** 2 + (0 - point2) ** 2)
            distances[point1, point2] = result

        # sorting
        sorted_points = sorted(distances, key=lambda p: distances[p])
            
        return [list(point) for point in sorted_points[:k]]

