from main import printLinkedList, convertArrayToLinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertNodeAtGivenPosition(head, position, val):
    node = Node(val)

    if position == 0:
        node.next = head
        return node

    currentNode = head
    count = 0
    previousNode = None

    while currentNode:
        if count == position:
            previousNode.next = node
            node.next = currentNode
            return head
        previousNode = currentNode
        currentNode = currentNode.next
        count += 1

    previousNode.next = node
    return head


def insertNodeBeforeValue(head, val, new_val):
    node = Node(new_val)
    if head.data == val:
        node.next = head
        return node

    previousNode = None
    currentNode = head
    while currentNode:
        if currentNode.data == val:
            previousNode.next = node
            node.next = currentNode
            return head

        previousNode = currentNode
        currentNode = currentNode.next

    return head


def insertNodeInLinkedList(head, data):
    if head == None:
        return

    node = Node(data)
    node.next = head

    return node


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    head = convertArrayToLinkedList(array)
    head = insertNodeAtGivenPosition(head, 5, 6)
    printLinkedList(head)
