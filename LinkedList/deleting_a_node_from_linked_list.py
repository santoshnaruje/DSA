from main import convertArrayToLinkedList, printLinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteTail(head):
    if not head:
        return None

    if not head.next:
        return head

    current = head

    while current.next.next:
        current = current.next
    current.next = None

    return head


def deleteByIndex(head, index):
    if not head:
        return None

    if index == 0:
        return head.next

    current = head
    previous = None
    count = 0
    while current:
        if count == index:
            previous.next = current.next
            return head
        previous = current
        current = current.next
        count += 1
    return head


def deleteByValue(head, value):
    if not head:
        return None

    if head.data == value:
        return head.next

    current = head
    previous = None

    while current:
        if current.data == value:
            previous.next = current.next
            return head
        previous = current
        current = current.next
    return head


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    head = convertArrayToLinkedList(array)
    # head = deleteTail(head)
    # printLinkedList(head)
    # deleteByValue(head, 3)
    # printLinkedList(head)
    head = deleteByValue(head,2)
    printLinkedList(head)