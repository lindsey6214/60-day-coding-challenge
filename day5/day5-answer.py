# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: 
    def hasCycle(self,head: ListNode) -> bool: 
        slow, fast = head, head 
        
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                return True
 
        return False

'''
Time complexity: O(n), where n is the number of nodes in the linked list. The slow pointer moves one step at a time, and the fast pointer moves two steps at a time. At each iteration of the while loop, we move the pointers by one or two steps, so we can visit each node in the linked list at most twice. Therefore, the time complexity of the solution is O(n).
Space complexity: O(1), since we keep up to the entire tree. In the solution, we use only two pointers slow and fast, and a few constant variables to store the head of the linked list and to iterate through the linked list. The number of variables we use does not depend on the size of the linked list, but only on the number of pointers we need to keep track of. Therefore, the space complexity of the solution is O(1).

Some mistakes I made sure not to make:
- Forgetting to check if the linked list is empty: in the while loop condition, we need to make sure to check if fast and fast.next are not None before accessing their next nodes. If we forget to do this, we may end up with a runtime error when trying to access a None object. 
- Incorrect initialization of the pointers: the slow and fast pointers need to be initialized to the head of the linked list. If we initialize them to None or some other value, we will not be able to traverse the linked list properly. 
- Incorrect logic for moving the pointers: we need to make sure to move the slow pointer one step at a time and the fast pointer two steps at a time. If we move them in the opposite direction or move them with different step sizes, we will not be able to detect the cycle in the linked list. 
- Incorrect comparison of the pointers: we need to compare the memory addresses of the slow and fast pointers to check if they point to the same node. If we compare their values, we will not be able to detect the cycle in the linked list. 
- Not returning False at the end: if the fast pointer reaches the end of the linked list without detecting a cycle, we need to return False. If we forget to do this, the function will not return anything or it will return an incorrect value. 
'''
