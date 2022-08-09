from classes import *
from classes.Tree import Tree

tree = Tree()
tree.addNodes(values=[1,2,3,2,4,2,5])
print(tree.levelTravel())