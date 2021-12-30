// Version 2 - DFS Improved
// Time complexity      O(n)
// Space complexity      O(n)
class Solution
{
public:
    void dfs(int node, vector<vector<int>> &graph, vector<int> &path, vector<vector<int>> &output)
    {
        path.push_back(node);
        if (node == graph.size() - 1) output.push_back(path);
        else
        {
            for (auto &next : graph[node])
            {
                dfs(next, graph, path, output);
            }
        }
        path.pop_back();
    }

    vector<vector<int>> allPathsSourceTarget(vector<vector<int>> &graph)
    {
        vector<vector<int>> output;
        vector<int> path;
        dfs(0, graph, path, output);
        return output;
    }
};

// Version 1 - DFS
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<int> path{0};
        return dfs(0, path, graph);
    }

    vector<vector<int>> dfs(int node, vector<int> path, vector<vector<int>>& graph)
    {
        vector<vector<int>> output;
        if (node == graph.size() - 1)
        {
            output.push_back(path);
        }
        else
        {
            for (auto& nextNode : graph[node] )
            {
                vector<int> pathIncNextNode(path);
                pathIncNextNode.push_back(nextNode);
                for (auto& childPath : dfs(nextNode, pathIncNextNode, graph))
                {
                    output.push_back(childPath);
                }
            }
        }
        return output
    }
};



// For edges connected to current node
// Append that edge to our current path
// Then call dfs on that node, giving it that path