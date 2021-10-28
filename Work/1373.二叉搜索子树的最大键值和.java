/*
 * @lc app=leetcode.cn id=1373 lang=java
 *
 * [1373] 二叉搜索子树的最大键值和
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int max = 0;
    public int maxSumBST(TreeNode root) {
        maxSumSubBST(root);
        
        return max;
    }
    void traverse(TreeNode root){
        ''' 1. 左右子树是否是BST
            2. 以当前节点为根的子树是否是BST
            3. 当前节点为根的BST子树键值和是多少
        '''
    }
}
// @lc code=end

