/*
 * @lc app=leetcode.cn id=797 lang=java
 *
 * [797] 所有可能的路径
 */

// @lc code=start
class Solution {
    List<List<Integer>> res = new LinkedList<>();

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        LinkedList<Integer> path = new LinkedList<>();
        traverse(graph, 0, path);
        return res;
    }

    void traverse(int[][] graph, int s, LinkedList<Integer> path){

        path.addLast(s);
        int n = graph.length;

        if(s == n-1){
            res.add(new LinkedList<>(path));
            path.removeLast();
            return;
        }

        for(int neighbor : graph[s]){
            traverse(graph, neighbor, path);
        }
        path.removeLast();

    }
}
// @lc code=end

