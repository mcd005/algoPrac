// TODO Explanation
// https://www.hackerrank.com/challenges/find-the-nearest-clone/

int findShortest(int graph_nodes, vector<int> graph_from, vector<int> graph_to, vector<long> ids, int val) {
    set<int> colours;
    bool pairFound = false;

    for (int i = 0; i < ids.size(); i++){
        if (colours.find(ids[i]) == colours.end()){
            colours.insert(ids[i]);
        }
        else{
            pairFound = true;
            break;
        }
    }
    if (pairFound == false) return -1;

    return 0;
}