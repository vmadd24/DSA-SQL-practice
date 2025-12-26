# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []
        merged_list_head = ListNode()
        temp = merged_list_head
        
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
                
        
        while min_heap:
            (val, i, elem) = heapq.heappop(min_heap)
            temp.next = elem
            temp = temp.next
            
            if elem.next:
                heapq.heappush(min_heap, (elem.next.val, i, elem.next))
        
        return merged_list_head.next
