class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class MyTree:
    def __init__(self, root):
        self.root = root

    def add_node(self, node):
        current = self.root

        while True:
            if node.data <= current.data:
                if current.left is None:
                    current.left = node
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                else:
                    current = current.right

    def __iter__(self):
        if self.root is None:
            stack = []
        else:
            stack = [self.root]
        return MyNodeIterator(stack)


class MyNodeIterator:

    def __init__(self, stack):
        self.stack = stack

    def __next__(self):
        if len(self.stack) <= 0:
            raise StopIteration
        current = self.stack.pop()
        data = current.data
        if current.right is not None:
            self.stack.append(current.right)
        if current.left is not None:
            self.stack.append(current.left)
        return data


if __name__ == '__main__':
    tree = MyTree(Node(16))
    tree.add_node(Node(8))
    tree.add_node(Node(1))
    tree.add_node(Node(17))
    tree.add_node(Node(24))
    tree.add_node(Node(13))
    tree.add_node(Node(14))
    tree.add_node(Node(9))
    tree.add_node(Node(10))
    tree.add_node(Node(11))

    for i in tree:
        print(i)

