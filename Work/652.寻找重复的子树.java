/*
 * @lc app=leetcode.cn id=652 lang=java
 *
 * [652] 寻找重复的子树
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
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        traverse(root);
        return res;
    }
    HashMap<String, Integer> memo = new HashMap<>();
    LinkedList<TreeNode> res = new LinkedList<>();
    String traverse(TreeNode root){
        if(root == null){
            return "#";
        }
        String subTree = traverse(root.left) + ',' + traverse(root.right) + ',' + root.val;
        int freq = memo.getOrDefault(subTree, 0);

        if(freq == 1){
            res.add(root);
            // System.out.println(res);
        }
        memo.put(subTree, freq + 1);
        return subTree;
    }
}
// @lc code=end

