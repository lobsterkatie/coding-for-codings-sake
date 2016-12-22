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


    def print_tree(self, node=None, level=0):
        """Prints out the tree, using indenting to indicate levels"""

        if not node:
            node = self.root

        print node.data

        if node.left_kid:
            print "  " * (level + 1) + "L:",
            self.print_tree(node.left_kid, level + 1)
        # else:
        #     print None

        if node.right_kid:
            print "  " * (level + 1) + "R:",
            self.print_tree(node.right_kid, level + 1)
        # else:
        #     print None

    def search_for(self, target_data, node="root"):
        """Walks the tree, looking for target_data; returns that data's Node if
           found, None if not."""

        if not node:
            return None

        if node == "root":
            node = self.root

        print "examining", node.data

        if node.data == target_data:
            print "found!"
            return node
        else:
            return (self.search_for(target_data, node.left_kid) or
                    self.search_for(target_data, node.right_kid))


#TODO - it's not this simple
    def penultimate(self):
        """Returns the second-highest node in the tree."""

        if not self.root:
            return None

        current_node = self.root
        prev_node = two_before = None


        while current_node:
            two_before = prev_node
            prev_node = current_node
            current_node = current_node.right_kid

        return two_before


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

print
tree.print_tree()


print
tree.search_for("e")

print
tree.search_for("h")
