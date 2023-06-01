class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if head == None or left == right:
            return head
        
        current = ListNode(-1, head)

        newHead = False
        if head.val == left:
            newHead = True

        while current.next.val != left:
            current = current.next

        newEnd = current.next
        begin = current
        middle = begin.next
        end = middle.next

        while middle.val != right:
            begin  = middle
            middle = end
            end = end.next
            middle.next = begin
        
        middle.next = begin
        current.next = middle
        newEnd.next = end

        if newHead:
            head = middle

        return head
    
    def print(self, head):
        while head != None:
            print(f"({head.val}) -> ", end="")
            head = head.next

solution = Solution()
head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
newHead = solution.reverseBetween(head, 0, 5)
solution.print(newHead)