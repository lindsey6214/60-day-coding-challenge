# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        return new_head

'''
Time complexity: O(n), where n is the number of nodes in the linked list. Since each node is visited exactly once during the recursion, the total number of recursive calls made by the function is equal to the number of nodes in the linked list. Therefore, the time complexity of the entire recursive process is O(n), where n is the size of the linked list. It's worth noting that each recursive call consumes some stack space due to the function call stack. For long linked lists, this could lead to a stack overflow. While the time complexity is O(n), the recursive approach might not be the most space-efficient method, especially for very long linked lists.
Space complexity: The space complexity in a recursive approach is determined by the maximum depth of the recursive call stack. In this case, for a linked list with n nodes, the recursive function reverseList is called n times (once for each node) until it reaches the base case (empty or single-node list). Each recursive call consumes additional stack space to store its local variables, parameters, and return address. Since the maximum depth of the call stack is equal to the number of nodes in the linked list, the space complexity is O(n). Therefore, in addition to the memory used for the linked list nodes themselves, the recursive approach requires O(n) extra memory for the call stack due to the recursive function calls.
While the recursive approach is conceptually straightforward, it might not be the most space-efficient method for very long linked lists, as it could lead to a stack overflow. For situations where memory usage is a concern, an iterative approach can be employed to achieve better space efficiency.
'''
