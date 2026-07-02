class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createLinkedList(nums):
    linkedList = Node(nums[0])
    linkedList.next = Node(nums[1])
    return linkedList


def convertArrayToLinkedList(nums):
    if not nums:
        return None

    head = Node(nums[0])
    mover = head
    for i in range(1, len(nums)):
        mover.next = Node(nums[i])
        mover = mover.next

    return head


def printLinkedList(linkedList):
    while linkedList:
        print(linkedList.data)
        linkedList = linkedList.next


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(createLinkedList(arr))
    linked_list = (convertArrayToLinkedList(arr))
    printLinkedList(linked_list)
