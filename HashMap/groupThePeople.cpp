class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        vector<vector<int>> res, groups(groupSizes.size() + 1);
        for (auto i = 0; i < groupSizes.size(); ++i) {
            groups[groupSizes[i]].push_back(i);
            if (groups[groupSizes[i]].size() == groupSizes[i]) {
                res.push_back({});
                swap(res.back(), groups[groupSizes[i]]);
            }
  }
  return res;
}
};