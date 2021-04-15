/*
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/
// Version 1 - Put each employee in a map then recursively DFS
// Time complexity      O(n)
// Space complexity     O(n)
class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        std::unordered_map<int, Employee*> employeeMap;

        for (auto emp: employees)
        {
            employeeMap[emp->id] = emp;
        }

        return dfs(id, employeeMap);
    }

    int dfs(int id, std::unordered_map<int, Employee*>& employeeMap)
    {
        Employee* currentEmployee = employeeMap[id];
        int sum = currentEmployee->importance;
        for (auto subId: currentEmployee->subordinates)
        {
            sum += dfs(subId, employeeMap);
        }
        return sum;
    }
};


