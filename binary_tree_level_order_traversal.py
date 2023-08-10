# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ### attempt 2
        # new recursion function: input node, depth, and cummulative list
        # list indices map directly to depth, entries in order left to right
        # base case: node = None
        # add curr value to list, left rec call, right rec call, each with depth + 1
        # no return, just mutates list
        def rec_depth(node, depth, depth_list):
            # base case
            if node is None:
                return
            # increase length of list when necessary
            if depth == len(depth_list):
                depth_list.append([])
            # add curr val, then recurse on left/right
            depth_list[depth].append(node.val)
            rec_depth(node.left, depth + 1, depth_list)
            rec_depth(node.right, depth + 1, depth_list)
        depth_list = []
        rec_depth(root, 0, depth_list)
        return depth_list
        
        ### attempt 1
        # # new recursion function: input node, depth, and cummulative dict
        # # dict maps from depth to list of nodes, in order left to right
        # # base cases: no left, no right => return dict
        # # left rec call, right rec call, each with depth + 1
        # # return updated dict
        # def rec_depth(node, depth, depth_dict):
        #     if node is None:
        #         return depth_dict
        #     # add left values
        #     if node.left is not None:
        #         depth_dict = rec_depth(node.left, depth + 1, depth_dict)
        #     # add curr value
        #     depth_dict[depth].append(node.val)
        #     # add right values
        #     if node.right is not None:
        #         depth_dict = rec_depth(node.right, depth + 1, depth_dict)
        #     return depth_dict
        # depth_dict = rec_depth(root, 0, defaultdict(list))
        # print(depth_dict)
        # return [tup[1] for tup in sorted(depth_dict.items(), key=lambda t: t[0])]
