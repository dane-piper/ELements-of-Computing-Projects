import os


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    # insert data into the tree
    def insert(self, data):
        new_node = Node(data)

        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root

            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            # found location now insert node
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        pass

    # Prints out all nodes at the given level
    def print_level(self, level):
        pass

    # Returns the height of the tree
    def get_height(self):
        pass

    # Returns the number of nodes in tree which is
    # equivalent to 1 + number of nodes in the left
    # subtree + number of nodes in the right subtree
    def num_nodes(self):
        pass


def main():


# write code here

main()