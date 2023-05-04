#Implementation of generic tree in Python

import random
import string
import pptree

class TreeNode(object):
    "Node of a Tree"
    def __init__(self, name='root', children=None,parent=None):
        self.name = name
        self.parent=parent
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def is_root(self):
        return self.parent is None
    def is_leaf():
        return len(self.children) == 0


    def depth(self):    # Depth of current node
        return 0 if self.is_root() else 1 + self.parent.depth()

    def add_child(self, node):
        node.parent=self
        assert isinstance(node, TreeNode)
        self.children.append(node)

    def disp(self):
        pptree.print_tree(self,'children','name')



class Tree:
    """
    Tree implemenation as a collection of TreeNode objects
    """
    def __init__(self):
       self.root=None
       self.height=0
       self.nodes=[]

    def insert(self,node,parent):   # Insert a node into tree
        if parent is not None:
            parent.add_child(node)
        else:
            if self.root is None:
                self.root=node
        self.nodes.append(node)

    def search(self,data):  # Search and return index of Node in Tree
        index=-1
        for N in self.nodes:
            index+=1
            if N.name == data:
                break
        if index == len(self.nodes)-1:
            return -1  #node not found
        else:
            return index

    def getNode(self,id):
        return self.nodes[id]

    def root():
        return self.root

#----------------------------------------------------------------------
# Binary TreeNode Implementation
class BinaryTreeNode(Tree):
    def __init__(self, name='root', children=None,parent=None):
       pass
#----------------------------------------------------------------------



##def getNodeRandom(node,level):
##    if level==1:
##        return node
##    else:
##        if(len(node.children) >0):
##            newnode=getNodeRandom(node.children[random.randint(0,len(node.children)-1)],level-1)
##            return newnode
##        else:
##            return node


##def TreeBuilder(steps):  # Random Tree Builder
##
##    root=TreeNode() #root node
##    depth=0
##
##
##    while(steps > 0):
##        #Randomly add tree nodes
##        tmax=random.randint(2,5)
##        depth=depth+1       #increase depth in each step
##        node2=getNodeRandom(root,depth)  #get a random node at current level
##        if node2 is None:
##            print("Invalid Node reached")
##            break
##
##        for i in range(tmax):
##            node2.add_child(TreeNode((random.choice(string.ascii_letters)+str(i)).upper()))
##
##        steps=steps-1
##
##    return root   # Returns root of Tree


def TreeBuilder2(steps):  # Random Tree Builder using Full Structure
    root=TreeNode('root')
    tree=Tree()
    tree.insert(root,None)

    for i in range(steps):
        tree.insert(TreeNode(random.choice(string.ascii_letters)+str(i)),tree.nodes[random.randint(0,len(tree.nodes)-1)])

    return tree


newtree=TreeBuilder2(50)
newtree.root.disp()
##root=TreeBuilder(10)
##root.disp()