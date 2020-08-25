# Concepts of LinkedLists


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_linkedlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


if __name__ == '__main__':

    # Cresting an object for the linkedlist class
    llist = LinkedList()

    # Creating 3 individual Nodes
    first = Node(1)
    second = Node(2)
    third = Node(3)

    # Linking the 3 nodes
    llist.head = first
    first.next = second
    second.next = third

    # Printing the data of all the nodes
    LinkedList.print_linkedlist(llist)
