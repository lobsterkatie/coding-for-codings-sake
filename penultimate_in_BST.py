class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.left_kid = None
        self.right_kid = None

    def __repr__(self):
        """Returns useful output when printing."""
        return "<Node {data}>".format(data=self.data)


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

    def find_max(self, node=None):
        """Returns the highest node in the tree, or in the subtree rooted at
           the given node."""

        #if the tree is empty, there is no max node
        if not self.root:
            return None

        #start looking at the given node, or the tree's root if no node is
        #given
        current_node = node or self.root
        prev_node = None

        #travel down the right side until there are no more right kids
        while current_node:
            prev_node = current_node
            current_node = current_node.right_kid

        #current_node is now the non-existent right child of prev_node;
        #prev_node must be the max because if there were any nodes greater than
        #it, they'd be off to its right
        #therefore, return prev_node
        return prev_node



#TODO - it's not this simple
    def penultimate(self):
        """Returns the second-highest node in the tree."""

        #if the tree is empty or if there's only one node, there is no
        #penultimate node
        if ((not self.root) or
            (not self.root.left_kid and not self.root.right_kid)):
            return None




        #go down to the right as far as possible
        current_node = self.root
        prev_node = two_before = None


        while current_node:
            two_before = prev_node
            prev_node = current_node
            current_node = current_node.right_kid

        #at this point, current_node is off the right side of the
        #bottom-right-most node of the current
        #continuously-descending-to-the-right chain, prev_node is that
        #bottom-right-most node, and two_before is prev_node's parent

        #prev_node is now by definition pointing to the biggest node in the
        #tree - if there were any nodes bigger, they'd be right descendants of
        #it, and by getting here we know that it has no more right descendants

        #there are now two possibilities: two_before

        #a candidate for the max in the tree, making two_before
        #a candidate for penultimate, and we know that prev_node doesn't have a
        #right child, but it's possible that it has a left_child, who would be
        #bigger than two_before but smaller than prev_node, making *it* a new
        #candidate for penultimate... unless of course it has any right
        #descendants, in which case one of them would be


        # current_node = self.root
        # prev_node = None

        # while current_node:
        #     current_node = current_node.right_kid




        # current_node = self.root
        # prev_node = two_before = None


        # while current_node:
        #     two_before = prev_node
        #     prev_node = current_node
        #     current_node = current_node.right_kid



        # return two_before


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")
i = Node("i")
j = Node("j")
k = Node("k")


tree = BST(a)
tree.insert_node(g)
tree.insert_node(f)
tree.insert_node(c)
tree.insert_node(e)
tree.insert_node(d)
tree.insert_node(b)
# tree.insert_node(h)
# tree.insert_node(i)
# tree.insert_node(j)
# tree.insert_node(k)


print
tree.print_tree()


print
print tree.search_for("e")

print
print tree.search_for("h")

print
print tree.find_max()


