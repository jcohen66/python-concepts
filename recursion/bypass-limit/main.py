class Node:
    def __init__(self, *children, data=None):
        self.children = list(children)
        self.data = data

    def __repr__(self):
        return f"({self.data})"


def print_parent_then_children1(node: Node, max_depth=-1):
    print(node)
    if max_depth == 0:
        return
    for child in node.children:
        print_parent_then_children1(child, max_depth - 1)


def print_parent_then_children2(node: Node, max_depth=-1):
    """Convert the recursive call stack into a literal
    call stack thereby making the process iterative.
    """
    stack = [(node, max_depth)]

    while stack:
        (node, max_depth) = stack.pop()

        print(node)
        if max_depth == 0:
            continue
        """Because its iterative add nodes
        to stack in reversed order.
        """
        for child in reversed(node.children):
            stack.append((child, max_depth - 1))


def walk_parent_then_children2(node: Node, max_depth=-1):
    """Convert the recursive call stack into a literal
    call stack thereby making the process iterative.
    """
    stack = [(node, max_depth)]

    while stack:
        (node, max_depth) = stack.pop()

        # Decouple using generator
        yield node
        if max_depth == 0:
            continue
        """Because its iterative add nodes
        to stack in reversed order.
        """
        for child in reversed(node.children):
            stack.append((child, max_depth - 1))


def small_sample():
    root = Node(
        Node(
            Node(data="child 0-0"),
            Node(data="child 0-1"),
            Node(data="child 0-2"),
            data="child 0",
        ),
        Node(data="child 1"),
        data="root",
    )
    # print_parent_then_children1(root, max_depth=1)
    print_parent_then_children2(root, max_depth=1)


if __name__ == "__main__":
    small_sample()
