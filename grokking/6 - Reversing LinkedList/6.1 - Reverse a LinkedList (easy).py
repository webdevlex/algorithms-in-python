from __future__ import print_function


# Define the Node class for the linked list
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")  # Use end=" " to separate values with a space
            temp = temp.next
        print()  # Print a newline after the linked list is printed


def reverse(head):
    # Initialize three pointers to reverse the linked list
    prev = None
    current = head
    while current is not None:
        next_node = current.next  # Store the next node temporarily
        current.next = prev  # Reverse the current node's pointer
        prev = current
        current = next_node
    return prev  # Return the new head of the reversed linked list


def main():
    # Create the original linked list
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)

    print("Nodes of the original LinkedList are: ", end=" ")
    head.print_list()

    result = reverse(head)  # Reverse the linked list

    print("Nodes of the reversed LinkedList are: ", end=" ")
    result.print_list()


if __name__ == "__main__":
    main()
