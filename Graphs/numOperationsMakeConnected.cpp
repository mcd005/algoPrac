class Solution
{
public:
    int makeConnected(int n, vector<vector<int> > &connections)
    {
        if (connections.size() < n - 1) return -1;

        pcToWhichNetwork.resize(n);
        std::iota(pcToWhichNetwork.begin(), pcToWhichNetwork.end(), 0);

        for (auto& conn : connections)
        {
            _union(conn[0], conn[1]);
        }

        return std::set<int>(pcToWhichNetwork.begin(), pcToWhichNetwork.end()).size() - 1;
    }
private:
    std::vector<int> pcToWhichNetwork;

    void _union(int x, int y)
    {
        pcToWhichNetwork[find(y)] = find(x);
    }

    int find(int a)
    {
        if (pcToWhichNetwork[a] != a)
        {
            return find(pcToWhichNetwork[a]);
        }
        return a;
    }
};

// n = 4, connections = [[0,1],[0,2],[1,2]]
// parents  = [0, 1, 2, 3]
// parents  = [0, 0, 0, 3]

// Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
// parents  = [0, 1, 2, 3, 4, 5]
// parents  = [0, 0, 0, 3, 4, 5]

// Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
// parents  = [0, 0, 0, 3, 0]

/*
Check that there are n - 1 cables
Union find to get all the islands
    Create a map whose keys are the PC number and the vals are the network number

    Then iterate over the connections
    If either PC is already connected (i.e. is not -1) then update our map
    Otherwise we create a new island
    conn[0] and conn[1] need to be set
Then number of changes you need to make is number of islands - 1
*/