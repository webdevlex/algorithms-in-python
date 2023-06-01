class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkedList(head):
        while head != None:
            print(f"({head.val}) -> ", end="")
            head = head.next

def linkedListComponents(head, nums):
        setG = set(nums)
        res = 0
        while head:
            if head.val in setG and (head.next == None or head.next.val not in setG):
                res += 1
            head = head.next
        return res

nums = [0,3,1,4]
head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))

result = linkedListComponents(head, nums)
print(result)