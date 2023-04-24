#
#				A
#		B 				C
#	D 		E 		F 		G
#
import node

def walk_preorder(tree):
    if tree is not None:
        print(tree)
        walk_preorder(tree.left)
        walk_preorder(tree.right)
        
def walk_inorder(tree):
    if tree is not None:
        walk_inorder(tree.left)
        print(tree)
        walk_inorder(tree.right)
        
def walk_postorder(tree):
    if tree is not None:
        walk_postorder(tree.left)
        walk_postorder(tree.right)
        print(tree)
        
        
if __name__ == "__main__":
    mytree = node.Node('A', node.Node('B', node.Node('D', node.Node('E', node.Node('C', node.Node('F', node.Node('G')))))))
 #   walk_preorder(mytree)
 #   walk_inorder(mytree)
    walk_postorder(mytree)
    