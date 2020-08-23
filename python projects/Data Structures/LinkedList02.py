# Dynamic Allocation of LinkedLists


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None

    def insert(self, val):
        temp = Node(val)
        root = self.head
        if self.head == None:
            self.head = temp
        else:
            while root.next != None:
                root = root.next
            root.next = temp

    def print_linkedlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


if __name__ == '__main__':

    # Creating a Head node
    llist = Linkedlist()

    # Getting User Input
    numbers = list(map(int, input("Enter Numbers: ").split()))

    # Creating and Linking each node
    for i in numbers:
        Linkedlist.insert(llist, i)

    # Displaying each Node in a linkedlist
    Linkedlist.print_linkedlist(llist)
