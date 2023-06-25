from exercise.TreeBasics.LC110BalancedBinaryTree import Solution
from model.BinaryTreeFromArray import BinaryTreeFromArray
import unittest


class TestBalancedBinaryTree(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        tree = BinaryTreeFromArray()
        root1 = tree.generateBinaryTree([3,9,20,None,None,15,7])
        self.assertEqual(s.isBalanced(root1), True)

    def test_case_2(self):
        s = Solution()
        tree = BinaryTreeFromArray()
        root = tree.generateBinaryTree([1,2,2,3,3,None,None,4,4])
        self.assertEqual(s.isBalanced(root), False)

    def test_case_3(self):
        s = Solution()
        tree = BinaryTreeFromArray()
        root = tree.generateBinaryTree([])
        self.assertEqual(s.isBalanced(root), True)

    def test_case_4(self):
        s = Solution()
        tree = BinaryTreeFromArray()
        root = tree.generateBinaryTree([1,2,2,3,None,None,3,4,None,None,4])
        self.assertEqual(s.isBalanced(root), False)

    def test_case_5(self):
        s = Solution()
        tree = BinaryTreeFromArray()
        root = tree.generateBinaryTree([1,None,2,None,3])
        self.assertEqual(s.isBalanced(root), False)
