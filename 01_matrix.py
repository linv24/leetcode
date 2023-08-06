class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # ### BFS solution
        # m, n = len(mat), len(mat[0])
        # queue = []
        # for r in range(m):
        #     for c in range(n):
        #         if mat[r][c] == 0:
        #             # append zero tiles
        #             queue.append((r,c))
        #         else:
        #             # replace 1 with -1 (not processed)
        #             mat[r][c] = -1

        # ptr = 0
        # visited = set()
        # while ptr < len(queue):
        #     r, c = queue[ptr]
        #     ptr += 1
        #     if (r,c) in visited:
        #         continue 
        #     visited.add((r,c))
        #     neighbors = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
        #     for new_r, new_c in neighbors:
        #         # if neighbor out of bounds, skip
        #         if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n: 
        #             continue
        #         if mat[new_r][new_c] == -1:
        #             mat[new_r][new_c] = mat[r][c] + 1
        #         else:
        #             mat[new_r][new_c] = min(mat[new_r][new_c], mat[r][c] + 1)
        #         queue.append((new_r, new_c))
        # return mat

        ### DP solution
        m, n = len(mat), len(mat[0])
        # min distance in any tile is the min of its smallest neighbor + 1
        # cannot compute 4 neighbors' distance simultaneously, so break into two steps:
        # start from top left, compute min distance of top and left neighbors only
        # (can guarantee those distances are already computed)
        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r-1][c] if r > 0 else math.inf
                    left = mat[r][c-1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1
        # start from bottom right, compute min distance of bottom and right neighbors only
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r+1][c] if r < m-1 else math.inf
                    right = mat[r][c+1] if c < n-1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)
        return mat
        
