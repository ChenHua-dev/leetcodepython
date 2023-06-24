from exercise.TreeBasics.LC144PreorderTraversal import Solution
from model.TreeNode import TreeNode
import unittest


class TestPreorderTraversal:
    def test_case_1(self):
        root = TreeNode(1)
        rootL = TreeNode(None)
        rootR = TreeNode(2)
        root.left = rootL
        root.right = rootR
        rootR.left = TreeNode(3)




