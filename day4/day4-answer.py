class Solution: 
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        stack = [] 
        prev = None 
        while stack or root: 
            while root: 
                stack.append(root) 
                root = root.left 
            root = stack.pop() 
            if prev and root.val <= prev.val: 
                return False 
            prev = root 
            root = root.right 
        return True

'''
Time complexity: O(n), the worst case when the tree is BST or the "bad" element is a rightmost leaf. 
Space complexity: O(1), since we keep up to the entire tree.

This is an example of a depth-first search (DFS) approach using an inorder traversal. In this solution, you visit the left subtree first, then the current node, and then the right subtree. By checking that each visited node has a value greater than the previously visited node, we ensure that the tree is a valid BST.
'''
