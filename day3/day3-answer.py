# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: ‘TreeNode’, p: ‘TreeNode’, q: ‘TreeNode’) -> ‘TreeNode’:
        cur=root

        While cur: 
            if p.val > cur.val and  q.val > cur.val:
                cur = cur.right 
            elif p.val < cur.val and  q.val < cur.val: 
                cur = cur.left 
            else:
                return cur 

'''
Time complexity: O(h), where h is the height of the tree. 
Space complexity: O(1), since we only use a constant amount of extra memory for the cur variable.

Things I kept in mind:
1) cur is not an ancestor of itself. To fix this, we can add a special case to return cur if it matches either p or q, but not both. 
2) One common mistake is to compare the val attribute of the nodes instead of the left and right pointers while traversing the tree. This will not work correctly, especially when the nodes have duplicate values. 
'''
