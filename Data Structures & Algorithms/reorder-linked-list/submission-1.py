class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list using slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next #end of first half 
            fast = fast.next.next #end of second half
            
        # Step 2: Reverse the second half of the list
        prev = None
        curr = slow.next #begining of second half
        slow.next = None  # Cut the first half from the second half
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # Step 3: Merge the two halves (head and prev)
        first, second = head, prev
        while second: # second can be shorter than first half
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2