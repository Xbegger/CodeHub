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
    int maxSum;
    public int maxSumBST(TreeNode root) {
        maxSum = 0;
        traverse(root);
        return maxSum;
    }
    int[] traverse(TreeNode root){
        /* 1. 左右子树是否是BST
            2. 以当前节点为根的子树是否是BST
            3. 当前节点为根的BST子树键值和是多少
        */
        if(root == null){
            return new int[]{
                1, Integer.MAX_VALUE, Integer.MIN_VALUE, 0
            };
        }

        int[] left = traverse(root.left);
        int[] right = traverse(root.right);

        int[] res = new int[4];
        // 判断左右子树是否是BST
        if(left[0] == 1 && right[0] == 1){
            // 判断当前节点为根的子树是否是BST
            if(root.val > left[2] && root.val < right[1]){
                res[0] = 1;
                res[1] = Math.min(left[1], root.val);
                res[2] = Math.max(right[2], root.val);
                // 计算当前节点为根的BST子树键值和
                res[3] = left[3] + right[3] + root.val;
                maxSum = Math.max(maxSum, res[3]);
            }else{
                res[0] = 0;
            }
        }

        return res;
    }
}
// @lc code=end

