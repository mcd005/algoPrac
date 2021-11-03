class Solution
{
public:
    int makeConnected(int n, vector<vector<int> > &connections)
    {
        if (connections.size() < n - 1) return -1;

        std::unordered_map<int, int> pcToWhichNetwork;
        int networkNumber = 0
        for (auto& conn : connections)
        {
            if (pcToWhichNetwork.count(conn[0]) > 0)
            {
                pcToWhichNetwork[conn[1]] = pcToWhichNetwork[conn[0]];
            }
            else if (pcToWhichNetwork.count(conn[1]) > 0)
            {
                pcToWhichNetwork[conn[0]] = pcToWhichNetwork[conn[1]];
            }
            else
            {
                network
            }
        }
    }
};

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