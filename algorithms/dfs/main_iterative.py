#
#				A
#		B 				C
#	D 		E 		F 		G
#
import node

def walk_preorder(tree, stack):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(node)
            stack.append(node.right)
            stack.append(node.left)
            
def walk_inorder(tree, stack):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            stack.append(node.right)
            print(node)
            stack.append(node.left)
            
def walk_postorder(tree, stack):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            stack.append(node.right)
            stack.append(node.left)
            print(node)
            
if __name__ == "__main__":
    stack = []
    mytree = node.Node('A', node.Node('B', node.Node('D', node.Node('E', node.Node('C', node.Node('F', node.Node('G')))))))

    walk_preorder(mytree, stack)
    print('-')
    walk_inorder(mytree, stack)
    print('-')
    walk_postorder(mytree, stack)