# Given the head of a Singly LinkedList, write a method to return the middle
# node of the LinkedList. If the total number of nodes in the LinkedList is
# even, return the second middle node.
#
# Example 1:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3
#
# Example 2:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Output: 4
#
# Example 3:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
# Output: 4


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def find_middle_of_linked_list(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)

    middle_node = find_middle_of_linked_list(head)
    print("Middle Node:", middle_node.value)


main()
