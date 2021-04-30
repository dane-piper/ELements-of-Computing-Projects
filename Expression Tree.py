import os

operators = ['+', '-', '*', '/', '//', '%', '**']


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


# self.parent = None
# self.visited = False
class Tree(object):
    def __init__(self):
        self.root = None

    def create_tree(self, expr):
        tokens = []
        stack = Stack()
        self.root = Node(None)
        current = self.root
        exp = ''
        for token in expr:
            if token == ' ':
                tokens.append(exp)
                exp = ''
            else:
                exp += token
        for token in tokens:
            if token == '(':
                new_node = Node(None)
                current.lchild = new_node
                stack.push(current)
                print(stack.size())
                current = current.lchild
            elif token in operators:
                current.data = token
                stack.push(current)
                print(stack.size())
                current.rchild = Node(None)
                current = current.rchild
            elif token == ')':
                if stack.size != 0:
                    current = stack.pop()
                    print(stack.size())
            else:
                current.data = token
                current = stack.pop()
                print(stack.size())

    def evaluate(self, aNode):
        if aNode.data not in operators:
            return float(aNode.data)
        else:
            if aNode.data == '+':
                return self.evaluate(aNode.lchild) + self.evaluate(aNode.rchild)
            if aNode.data == '-':
                return self.evaluate(aNode.lchild) - self.evaluate(aNode.rchild)
            if aNode.data == '*':
                return self.evaluate(aNode.lchild) * self.evaluate(aNode.rchild)
            if aNode.data == '/':
                return self.evaluate(aNode.lchild) / self.evaluate(aNode.rchild)
            if aNode.data == '//':
                return self.evaluate(aNode.lchild) // self.evaluate(aNode.rchild)
            if aNode.data == '%':
                return self.evaluate(aNode.lchild) % self.evaluate(aNode.rchild)
            if aNode.data == '**':
                return self.evaluate(aNode.lchild) ** self.evaluate(aNode.rchild)
    def pre_order(self, aNode):
        if aNode.lchild is None:
            return aNode.data + ' '
        else:
            return aNode.data + ' ' + self.pre_order(aNode.lchild) + self.pre_order(aNode.rchild)


    def post_order(self, aNode):
        if aNode.lchild is None:
            return aNode.data
        else:
            return self.post_order(aNode.lchild) + ' ' + self.post_order(aNode.rchild) + ' ' + aNode.data


def main():
    expr = '( ( 8 + 3 ) * ( 7 - 2 ) )'
    tree = Tree()
    tree.create_tree(expr)
    print(tree.evaluate(tree.root))
    print(tree.pre_order(tree.root))
    print(tree.post_order(tree.root))


main()