class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
printList(head)