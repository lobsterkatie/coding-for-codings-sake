class Node(object):
    """A node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        """Provide useful info when printed."""
        return "<Node {data}>".format(data=self.data)


class SinglyLinkedList(object):
    """A singly-linked list"""

    def __init__(self, head=None):
        self.head = head


    def swap_nodes(self, prev_node, node1, node2):
        """Swaps node1 and node2, so that node2 is before node1."""

        #if node1 is the head of the list
        if not prev_node:
            self.head = node2
        #otherwise
        else:
            prev_node.next = node2

        #do the rest of the swapping
        node1.next = node2.next
        node2.next = node1


    def sort_in_place(self):
        """Sorts the list in place."""

        prev_node = None
        current_node = self.head

        length = self.length()
        i = 0
        swap_happened = True

        #while things might still be out of order and we still have at least
        #two nodes to compare
        while swap_happened and i < (length - 1):
            print "pass", i

            swap_happened = False

            #while there are nodes left to examine in this pass
            while current_node.next:
                next_node = current_node.next
                #compare current and next to see if they need to be swapped
                if current_node.data > next_node.data:
                    print "swapping", current_node, "with", next_node
                    self.swap_nodes(prev_node, current_node, next_node)
                    swap_happened = True

                #move on to the next node
                prev_node = current_node
                current_node = next_node

            #get things ready for the next pass
            prev_node = None
            current_node = self.head
            i += 1


    def print_list(self):
        """Prints the content of the list"""

        data = []
        current_node = self.head

        while current_node:
            data.append(current_node.data)
            current_node = current_node.next

        print "list data:", data


    def length(self):
        """Return the length of the list"""

        current_node = self.head
        i = 0

        while current_node:
            i += 1
            current_node = current_node.next

        return i


#make a list to test the code
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

#the original list order is e, c, a, b, d
e.next = c
c.next = a
a.next = b
b.next = d

llist = SinglyLinkedList(e)

print
print "before sorting:"
llist.print_list()
print
print "sorting..."
llist.sort_in_place()
print
print "after sorting:"
llist.print_list()
print
