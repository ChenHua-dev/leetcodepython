from typing import List, Optional
from model.TreeNode import TreeNode


class BinaryTreeDiagram:
    """
           1
         /   \
       2       3
      / \     / \
     4   5   6   7
    """
    def getTreeHeight(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            lHeight = self.getTreeHeight(root.left)
            rHeight = self.getTreeHeight(root.right)
            return 1 + max(lHeight, rHeight)

    def writeArray(self, currNode: TreeNode, rowIndex: int , columnIndex: int , res: List[List[str]], treeDepth: int) -> None:
        # Base case: 保证输入的树不为空
        if not currNode:
            return

        # Recursive case: 先将当前节点保存到二维数组中
        res[rowIndex][columnIndex] = "" if not currNode else str(currNode.val)

        # 计算当前位于树的第几层
        currLevel = ((rowIndex + 1) // 2)
        # 若到了最后一层，则返回
        if currLevel == treeDepth:
            return
        # 计算当前行到下一行，每个元素之间的间隔（下一行的列索引与当前元素的列索引之间的间隔）
        gap = treeDepth - currLevel - 1

        # 对左儿子进行判断，若有左儿子，则记录相应的"/"与左儿子的值
        if currNode.left is not None:
            res[rowIndex + 1][columnIndex - gap] = "/"
            self.writeArray(currNode.left, rowIndex + 2, columnIndex - gap * 2, res, treeDepth)


        # 对右儿子进行判断，若有右儿子，则记录相应的"\"与右儿子的值
        if currNode.right is not None:
            res[rowIndex + 1][columnIndex + gap] = "\\"
            self.writeArray(currNode.right, rowIndex + 2, columnIndex + gap * 2, res, treeDepth)

    def show(self, root: Optional[TreeNode]) -> None:
        res = []
        if not root:
            print("EMPTY!")
            return
        if not root.left and not root.right:
            print(str(root.val))
            return
        else:
            # 得到树的深度
            treeDepth = self.getTreeHeight(root)
            # 最后一行的宽度为2的（n - 1）次方乘3，再加1
            # 作为整个二维数组的宽度
            arrayHeight = treeDepth * 2 - 1
            arrayWidth = (2 << (treeDepth - 2)) * 3 + 1
            # 用一个字符串数组来存储每个位置应显示的元素
            # res = []
            # 对数组进行初始化，默认为一个空格
            for _ in range(arrayHeight):
                row = []
                for _ in range(arrayWidth):
                    row.append(" ")
                res.append(row)
            # 从根节点开始，递归处理整个树
            # res[0][(arrayWidth + 1)/ 2] = (char)(root.val + '0');
            self.writeArray(root, 0, arrayWidth // 2, res, treeDepth)
            # 此时，已经将所有需要显示的元素储存到了二维数组中，将其拼接并打印即可
            for line in res:
                builder = ""
                for i in range(len(line)):
                    builder += line[i]
                    if len(line[i]) > 1 and i <= len(line) - 1:
                        i += 2 if len(line[i]) > 4 else len(line[i]) - 1
                print(str(builder))

