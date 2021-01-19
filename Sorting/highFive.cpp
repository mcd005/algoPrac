 // https://leetcode.com/problems/high-five/

/* 
Version 4 - Map of multisets
Time complexity     O(n * log k) for n insertions into a multiset whose size is k (max of 5)
Space complexity    O(n)
 */
class Solution {
    public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
        std::unordered_map<int, multiset<int>> dict;
        vector<vector<int>> output;

        for (auto item: items){
            multiset<int>* currentSet = &dict[item[0]];
            currentSet->insert(item[1]);
            if (currentSet->size() > 5) currentSet->erase(currentSet->begin());
        }

        for (auto &i: dict){
            int currentStuSum = 0;
            for (auto j: i.second){
                currentStuSum += j;
            }
            output.emplace_back(vector<int>{i.first, currentStuSum / 5});
        }
        
        //Need to return the output in order of student IDs
        sort(output.begin(), output.end(), [](const vector<int> &l, const vector<int> &r) {
            return l[0] < r[0];    
        });

        return output;
    }
};

/* 
Version 3 - Count sort because scores are of the set {1, 2, 3... 100}
This was fairly heavily borrowed from the Leetcode discussion boards
I kept it because I liked the "sum += min(c, s[i])" trick
Time complexity     O(n)
Space complexity   O(n)
*/
class Solution {
    public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
        //This is will be vector will contain one counter array per student
        //Where a counter array is 101 elemtents long
        vector<vector<int>> scores;
        
        for (auto i : items) {
            //For each ID, we make sure is a space in our array at least that many counters
            if (scores.size() < i[0]) scores.resize(i[0]);
            //We also make sure the counter is initalised to the right size
            if (scores[i[0] - 1].empty()) scores[i[0] - 1].resize(101);
            ++scores[i[0] - 1][i[1]];
        }
    
        vector<vector<int>> res;
        for (auto s : scores) {
            auto sum = 0;
            for (auto i = 100, c = 5; c > 0; --i) {
                //Let's say a student got at least 6 scores that were 100s
                //These line lets us add them all to his top 5 total straight away
                //rather than decerememting through them 1-by-1 as we ususally would with a count sort
                sum += min(c, s[i]) * i;  
                c -= s[i];
            }   
        res.push_back({static_cast<int>(res.size()) + 1, sum / 5 });
        }
    return res;
    }
};

/* 
Version 2 - Partial Sort
Time complexity     O(nlogk) is the time complexity of partial sort where k is 5
Space complexity    O(n)
 */
class Solution {
public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
       vector<vector<int>> output;

       map<int, vector<int>> idDict;
        
       for (auto& v : items){
            idDict[v[0]].emplace_back(v[1]);
       }
    
       for (auto& [i, v] : idDict) {
           //We then partial sort each list of scores to get the top 5 scores
           partial_sort(v.begin(), v.begin() + 5, v.end(), greater<int>());
           output.push_back({ i, (v[0] + v[1] + v[2] + v[3] + v[4]) / 5 });
       }
       return output;
    }
};

/* 
Version 1 - Sort the entire input array
Time Complexity     O(nlogn)
Space complexity    O(n)
 */
class Solution {
public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
        vector<vector<int>> output;
        
        //This map will look like {Student ID : [number of scores recorded for this student, sum of scores so far]}
        map<int, vector<int>> idDict;
        
        //Sort the whole array in place, in descending order of score
        //This way we encounter each students top 5 scores first
        sort(items.begin(), items.end(), [](vector<int> a, vector<int> b){
            return a[1] > b[1];
        });
        
        int n = items.size();
        for (int i = 0; i < n; ++i){
            int id = items[i][0];
            int score = items[i][1];
            
            if (idDict.find(id) != idDict.end()){
                //Check that we are not recording more than five scores per student
                if (idDict[id][0] < 5){
                    idDict[id][1] += score;
                    idDict[id][0]++;
                }
            }
            else{
                vector<int> student{1, score};
                idDict.insert({ id , student });
            }
        }
        
        for (auto const& [key, val] : idDict){
            vector<int> studentAverage{key, val[1] / 5};
            output.push_back(studentAverage);
        }
        
        return output;
    }
};

