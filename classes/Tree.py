'''
Author: error: git config user.name && git config user.email & please set dead value or install git
Date: 2022-08-09 11:34:25
LastEditors: error: git config user.name && git config user.email & please set dead value or install git
LastEditTime: 2022-08-09 15:14:19
FilePath: \1\Tree.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from collections import deque

res = deque()

# CLASS: 节点对象
class Node():

    # FUNCTION: 初始化叶子节点
    def __init__(self, value: int=0) -> None:
        self.val = value
        self.left, self.right = None, None
        pass

# CLASS: 二叉树对象
class Tree():

    # FUNCTION: 初始化根节点
    def __init__(self) -> None:
        self.root = None
        pass

    # FUNCTION: 空树判断
    def isEmpty(self) -> bool:
        if self.root == None:
            return True
        else:
            return False
        pass

    # FUNCTION: 插入单个节点
    def addNode(self, value: int) -> None:

        # MODULE: 空树判断
        if self.isEmpty():
            self.root = Node(value)
            return
        
        # MODULE: 添加节点
        # 维护一个节点队列
        queue = deque()
        # 初始将根节点入队
        queue.append(self.root)
        while True:

            # 出队
            current = queue.popleft()

            # MODULE: 尝试加入左孩子
            if current.left == None:
                current.left = Node(value)
                break
            else:
                queue.append(current.left)

            # MODULE: 尝试加入右孩子
            if current.right == None:
                current.right = Node(value)
                break
            else:
                queue.append(current.right)
        pass
                
    # FUNCTION: 插入多个节点
    def addNodes(self, values: list) -> None:

        for value in values:
            self.addNode(value)
        pass

    # FUNCTION: 层次遍历
    def levelTravel(self) -> deque:

        # MODULE: 空树判断
        if self.isEmpty():
            return

        # MODULE: 遍历节点
        # 通过维护队列遍历到每一个节点
        res, queue = deque(), deque()
        # 初始化加入根节点
        queue.append(self.root)

        # 当节点队列为空时推出循环
        while queue:
            # 出队
            current = queue.popleft()
            # 将当前值加在res上
            res.append(current.val)
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)

        return res 
        pass

    # FUNCTION: 先序遍历
    def initialTravel(self) -> deque: 

        global res

        def iniT(node) -> None:

            global res
            
            # MODULE: 递归终止
            if node == None:
                return
            
            # MODULE: 递归进行
            res.append(node.val)
            iniT(node.left)
            iniT(node.right)
        
        iniT(self.root)

        # MODULE: 清洗全局变量   
        result = res
        res = deque()

        return result
        pass

    # FUNCTION: 中序遍历
    def middleTravel(self) -> deque:   
       
        global res
        
        def midT(node) -> None:

            global res

            # MODULE: 递归终止
            if node == None:
                return
            
            # MODULE: 递归进行
            midT(node.left)
            res.append(node.val)
            midT(node.right)
        
        midT(self.root)

        # MODULE: 清洗全局变量
        result = res
        res = deque()

        return result
        pass

    # FUNCTION: 后序遍历
    def finalTravel(self) -> deque:

        global res

        def finT(node) -> None:

            global res
            
            # MODULE: 递归终止
            if node == None:
                return
            
            # MODULE: 递归进行
            finT(node.left)
            finT(node.right)
            res.append(node.val)
        
        finT(self.root)

        # MODULE: 清洗全局变量   
        result = res
        res = deque()

        return result
        pass

if __name__ == "__main__":
    
    t = Tree()
    t.addNodes([0,3,6,2,4,2])
    
    print(t.levelTravel())
    print(t.initialTravel())
    print(t.middleTravel())
    print(t.finalTravel())