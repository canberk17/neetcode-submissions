# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        
        def mergeLists(lists,s,e):
            
            if s==e:
                return lists[s]
            
            m = (s+e)//2

            left = mergeLists(lists,s,m)
            right= mergeLists(lists,m+1,e)

            return merge(left,right)
        
        def merge(left,right):
            dummy = ListNode(0)
            curr = dummy

            while left and right:
                if left.val < right.val:
                    curr.next=left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            
            while left:
                curr.next =left
                left = left.next
                curr = curr.next
            while right:
                curr.next=right
                right = right.next
                curr = curr.next
            return dummy.next
        return mergeLists(lists,0,len(lists) - 1)




            