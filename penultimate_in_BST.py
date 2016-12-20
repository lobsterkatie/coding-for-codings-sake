class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.left_kid = None
        self.right_kid = None




class BST(object):
    """A basic binary search tree. Currently not self-balancing, and assumes
       all nodes have distinct data."""

    def __init__(self, root=None):
        self.root = root

    def insert_node(self, new_node):
        """Inserts the given node in the appropriate place."""

        print "inserting", new_node.data

        #if the tree is empty, the make the node to be inserted its root
        if not self.root:
            self.root = new_node
            return

        #otherwise, start at the root and traverse the tree until we find where
        #to put the given node

        direction = None
        prev_node = None
        current_node = self.root

        while current_node:
            #keep track of where we just were
            prev_node = current_node

            #if the new node is less than the current one, move down and to the
            #left
            if new_node.data < current_node.data:
                direction = "L"
                current_node = current_node.left_kid

            #otherwise, if it's greater, move down and to the right
            elif new_node.data > current_node.data:
                direction = "R"
                current_node = current_node.right_kid

        #if we've broken out of the loop, that means we've found an empty spot
        #(because current_node is None), so insert the new node there
        if direction == "L":
            prev_node.left_kid = new_node
        elif direction == "R":
            prev_node.right_kid = new_node


    def print_tree(self, node=None, indent=None, direction=None):
        """Prints out the tree, using indenting to indicate levels"""

        if not node:
            node = self.root

        if not indent:
            indent = 3

        # if direction == "L":
        #     indent -= 2
        # elif direction == "R":
        #     indent = 2 * level
        # else:
        #     indent = 3
        print " " * indent + str(node.data)

        #     print " " * (level * 2) + str(node.data)
        # else:
        #     print "   " + str(node.data)

        if node.left_kid:
            print " " * (indent - 1) + "/"
            self.print_tree(node.left_kid, indent - 2, "L")
        # else:
        #     print None

        if node.right_kid:
            print " " * (indent + 1) + "\\"
            self.print_tree(node.right_kid, indent + 2, "R")
        # else:
        #     print None

        print


a = Node("a")
b = Node("b")
f = Node("f")
d = Node("d")
c = Node("c")
e = Node("e")
g = Node("g")


tree = BST(d)
tree.insert_node(a)
tree.insert_node(f)
tree.insert_node(c)
tree.insert_node(e)
tree.insert_node(b)
tree.insert_node(g)


tree.print_tree()
