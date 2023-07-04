from MinimalTree import *


def bstSequence(root):
    if root == None:
        return [LinkedList()]

    leftList = bstSequence(root.left)
    rightList = bstSequence(root.right)

    prefix = LinkedList()
    prefix.insert(root.value)

    result = []
    for list1 in leftList:
        for list2 in rightList:
            weave(list1, list2, result, prefix)
    return result


def weave(list1, list2, result, prefix):
    if list1.empty() or list2.empty():
        listToAppend = LinkedList()
        if not list1.empty():
            listToAppend.copy(list1)
        elif not list2.empty():
            listToAppend.copy(list2)

        prefixCopy = LinkedList()
        prefixCopy.copy(prefix)
        prefixCopy.appendList(listToAppend)
        result.append(prefixCopy)
        return

    head1 = list1.removeFront()
    prefix.insertNode(head1)
    weave(list1, list2, result, prefix)
    end1 = prefix.removeEnd()
    list1.insertFront(end1)

    head2 = list2.removeFront()
    prefix.insertNode(head2)
    weave(list1, list2, result, prefix)
    end2 = prefix.removeEnd()
    list2.insertFront(end2)


class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def removeFront(self):
        if not self.empty():
            head = self.head
            if self.head == self.end:
                self.head = None
                self.end = None
            else:
                self.head = self.head.next
                self.head.prev = None
                head.next = None
            return head

    def removeEnd(self):
        if not self.empty():
            if self.head == self.end:
                self.head = None
                self.end = None
            else:
                end = self.end
                self.end = self.end.prev
                end.prev = None
                self.end.next = None
                return end

    def insert(self, value):
        newNode = Node(value)
        if self.empty():
            self.head = newNode
            self.end = newNode
        else:
            self.end.next = newNode
            newNode.prev = self.end
            self.end = newNode

    def insertNode(self, newNode):
        if self.empty():
            self.head = newNode
            self.end = newNode
        else:
            self.end.next = newNode
            newNode.prev = self.end
            self.end = newNode

    def insertFront(self, newNode):
        if self.empty():
            self.head = newNode
            self.end = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def copy(self, listToCopy):
        current = listToCopy.head

        if current == None:
            self.head = None
            self.end = None
        else:
            newNode = Node(current.value)
            self.head = newNode
            while current.next != None:
                current = current.next
                newNode.next = Node(current.value)
                newNode.next.prev = newNode
                newNode = newNode.next
            self.end = newNode

    def empty(self):
        return self.head == None and self.end == None

    def appendList(self, listToAppend):
        if not listToAppend.empty():
            if self.empty():
                self.head = listToAppend.head
            else:
                self.end.next = listToAppend.head
                listToAppend.prev = self.end
            self.end = listToAppend.end

    def print(self):
        current = self.head
        while current != None:
            print(f"({current.value}) -> ", end="")
            current = current.next
        print("")


class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


valid = [1, 3, 4, 5, 6, 7, 8]
root = binaryTree(valid)
allLists = bstSequence(root)

for list in allLists:
    list.print()
