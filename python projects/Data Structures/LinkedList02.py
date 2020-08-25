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
    n = int(input("Enter number of elements to be added: "))

    # Creating and Linking each node
    for i in range(1, n+1):
        print("Enter value%d: " % i, end='')
        value = input()
        Linkedlist.insert(llist, value)

    # Displaying each Node in a linkedlist
    Linkedlist.print_linkedlist(llist)
