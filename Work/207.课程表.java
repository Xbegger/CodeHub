/*
 * @lc app=leetcode.cn id=207 lang=java
 *
 * [207] 课程表
 */

// @lc code=start
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = buildGraph(numCourses, prerequisites);
        visited = new boolean[numCourses];
        onPath = new boolean[numCourses];
        boolean res = true;
        for(int i=0; i<numCourses ; i++){
            res = traverse(graph, i) && res; 
        }
        return res;
    }
    boolean[] visited;
    boolean[] onPath;
    boolean traverse(List<Integer>[] graph, int s){

        boolean ans = true;
        if(onPath[s] == true){
            return false;
        }
        if(visited[s] == true){
            return true;
        }
        visited[s] = true;
        onPath[s] = true;
        for(int v : graph[s]){
            ans = ans && traverse(graph, v);
        }
        onPath[s] = false;

        return ans;
    }
    List<Integer>[] buildGraph(int numCourses, int[][] prerequisites) {
        // 图中共有 numCourses 个节点
        List<Integer>[] graph = new LinkedList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new LinkedList<>();
        }
        for (int[] edge : prerequisites) {
            int from = edge[1];
            int to = edge[0];
            // 修完课程 from 才能修课程 to
            // 在图中添加一条从 from 指向 to 的有向边
            graph[from].add(to);
        }
        return graph;
    }  
}
// @lc code=end

