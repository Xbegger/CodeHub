/*
 * @lc app=leetcode.cn id=105 lang=java
 *
 * [105] 从前序与中序遍历序列构造二叉树
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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return build(preorder, inorder, 0, inorder.length);
    }
    int k=0;
    TreeNode build(int[] preorder, int[] inorder, int left, int right){
        if(left >= right){
            return null;
        }
        int rootNo = left;
        for(int i=left; i<right ; i++){
            if(inorder[i] == preorder[k]){
                rootNo = i;
                break;
            }
        }
        TreeNode root = new TreeNode(preorder[k]);
        k = k+1;
        System.out.println("left:" + left + "right:" + right);
        root.left = build(preorder, inorder, left, rootNo);
        root.right = build(preorder, inorder, rootNo + 1, right);
        return root;
    }
}
// @lc code=end

