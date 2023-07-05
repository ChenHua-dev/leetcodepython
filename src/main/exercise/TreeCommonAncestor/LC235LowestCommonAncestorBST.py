from model.BinaryTreeDiagram import BinaryTreeDiagram
from model.BinaryTreeFromArray import BinaryTreeFromArray
from model.TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        root_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val == root_val or q_val == root_val:
            return root
        if p_val > root_val and q_val > root_val:
            root = self.lowestCommonAncestor(root.right, p, q)
        if p_val < root_val and q_val < root_val:
            root = self.lowestCommonAncestor(root.left, p, q)

        return root


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTreeFromArray()
    diagram = BinaryTreeDiagram()
    root1 = tree.generateBinaryTree([6,2,8,0,4,7,9,None,None,3,5])
    root2 = tree.generateBinaryTree([6,2,8,0,4,7,9,None,None,3,5])
    root3 = tree.generateBinaryTree([2,1])
    diagram.show(root1)
    print()
    diagram.show(root2)
    print()
    diagram.show(root3)
    print()
    print(s.lowestCommonAncestor(root1, TreeNode(2), TreeNode(8)).val)
    print(s.lowestCommonAncestor(root2, TreeNode(2), TreeNode(4)).val)
    print(s.lowestCommonAncestor(root3, TreeNode(2), TreeNode(1)).val)

