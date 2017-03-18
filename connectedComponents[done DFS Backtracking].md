[Note]
====== 

[Problem]
====== 
Find the Connected Component in the Undirected Graph

Find the number connected component in the undirected graph. Each node in the graph contains a label and a list of its neighbors. 
(a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

Example
Given graph:



Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}

[code]
======
```java

Solution
/**
 * Definition for Undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    /**
     * @param nodes a array of Undirected graph node
     * @return a connected set of a Undirected graph
     */
    HashSet<UndirectedGraphNode> set;
    public List<List<Integer>> connectedSet(ArrayList<UndirectedGraphNode> nodes) {
        // Write your code here
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        set = new HashSet<>();

        for (UndirectedGraphNode node : nodes) {
            if (!set.contains(node)) {
                ArrayList<Integer> path = new ArrayList<>();

                 dfs(node, path);
                 Collections.sort(path);
                result.add(path);
            }
        }
        return result;
    }
    void dfs(UndirectedGraphNode  node,  ArrayList<Integer> path) {
        if (set.contains(node)) return;
        path.add(node.label);
        set.add(node);

        for (UndirectedGraphNode cNode : node.neighbors) {
          //  path.add(cNode.label);
            //set.add(cNode);
            dfs(cNode, path);
        }
    }
}


/**
 * Definition for Undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
public:
    /**
     * @param nodes a array of Undirected graph node
     * @return a connected set of a Undirected graph
     */
    vector<vector<int>> connectedSet(vector<UndirectedGraphNode*>& nodes) {
        typedef UndirectedGraphNode Node;
        unordered_set<Node*> visited_nodes;
        function<void(Node*, vector<int>&)> dfs_visit = [&](Node* node, vector<int>& component) {
            if (visited_nodes.count(node)) {
                return;
            }
            component.push_back(node->label);
            visited_nodes.insert(node);
            for (auto next_node : node->neighbors) {
                dfs_visit(next_node, component);
            }
        };

        vector<vector<int> > ret;
        for (auto node : nodes) {
            if (!visited_nodes.count(node)) {
                vector<int> component;
                dfs_visit(node, component);
                sort(component.begin(), component.end());
                ret.push_back(component);
            }
        }
        return ret;
    }
};
```