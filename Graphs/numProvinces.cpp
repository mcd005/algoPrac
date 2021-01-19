// https://leetcode.com/problems/number-of-provinces/

// Version X and X++ - iterative
// Do a DFS with a stack or BFS with a queue for a super speedy algo

// Version 1 - depth first search
// Time complexity      O(n * n)    where n is the number of cities
// Space complexity     O(n)        n calls on the stack at most
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int provinces = 0;
        
        int n = isConnected.size();
        for (int i = 0; i < n; ++i){
            for (int j = 0; j < n; ++j){
                if (isConnected[i][j] == 1){
                    // We mark each visited element by overwriting it with -1 
                    // so that it's not double checked
                    isConnected[i][j] = -1;
                    // If we come across a city (represented by the 1s at i == j, because a city must be connected to self)
                    // and it's not yet been marked then we've found a new province
                    if (i == j){
                        ++provinces;
                    } 
                    else{
                        // Then we go ahead and mark off all the cities it's connected to 
                        // as part of the same province
                        markNeighbours(isConnected, j, n);
                    }
                }
            }
        }

        return provinces;
    }
    
    void markNeighbours(vector<vector<int>> &isConnected, int cityNo, int n){
        if (isConnected[cityNo][0] == -1) return;
        // We mark off cities recursively in a DFS:
        //      Look at the cities that the current city is connected to
        //      mark them off and look at the cities that those cities are connected to
        //      in turn mark *them* off and look at the cities that *they* are connected to
        //      and so on
        for (int k = 0; k < n; ++k){
            if (isConnected[cityNo][k] == 1){
                isConnected[cityNo][k] = -1;
                markNeighbours(isConnected, k, n);
            }
        }
    }
};