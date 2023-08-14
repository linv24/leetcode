"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # attempt 2: optimize
        # use dict as a seen tracker by referencing it when adding
        # neighbors to queue
        if node is None:
            return None
        q = deque([node])
        d = {node.val: Node(node.val)}
        while q:
            curr_old = q.popleft()
            curr_new = d[curr_old.val]
            for nb in curr_old.neighbors:
                if nb.val not in d:
                    d[nb.val] = Node(nb.val)
                    q.append(nb)
                curr_new.neighbors.append(d[nb.val])
        return d[node.val]

        # # attempt 1: BFS
        # # list to queue original graph, dict to map unique val
        # # to new graph nodes. at each original node, get new node 
        # # object from dict (or create new one), add neighbors 
        # # (referencing dict if exist already)
        # if node is None:
        #     return None
        # q = [node]
        # d = {}
        # seen = set()
        # ptr = 0
        # while ptr < len(q):
        #     curr_old = q[ptr]
        #     if curr_old.val not in seen:
        #         seen.add(curr_old.val)
        #         if curr_old.val not in d: 
        #             d[curr_old.val] = Node(curr_old.val)
        #         curr_new = d[curr_old.val]
        #         for n in curr_old.neighbors:
        #             if n.val not in d:
        #                 d[n.val] = Node(n.val)
        #             curr_new.neighbors.append(d[n.val])
        #         q.extend([n for n in curr_old.neighbors if n.val not in seen])
        #     ptr += 1
        # return d[node.val]
