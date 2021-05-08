// https://leetcode.com/problems/car-fleet-ii
// Version 1 - Stack
// Time complexity      O(n)
// Space complexity     O(n)
class Solution
{
public:
    vector<double> getCollisionTimes(vector<vector<int>> &cars)
    {
        int n = cars.size();
        vector<double> answer(n, 0.0);
        answer[n - 1] = -1.0;

        // This stack represents all the cars ahead of the current car that it could possibly catch up to
        stack<vector<double>> s; // 0 = position, 1 = speed, 2 = time intersects car ahead of it physically (which is a car below it in the stack)
        s.push({(double) cars[n - 1][0], (double) cars[n - 1][1], -1.0});

        for (int i = n - 2; i > -1; --i)
        {
            double intersectTime = -1.0;
            while (!s.empty())
            {
                // If the current car is the same speed or slower than the car ahead
                // it will never catch to the car ahead, unless the car ahead is blocked by a slower car
                // hence we pop the fast car off the stack
                if (cars[i][1] <= s.top()[1])
                {
                    s.pop();
                    continue;
                }
                
                // If the current car is faster than at least one the cars ahead, however,
                // then it will intersect that car at some time
                intersectTime = calculateIntersectTime(cars[i], s.top()[0], s.top()[1]);
                double carAheadIntersectTime = s.top()[2];
                if (carAheadIntersectTime > 0 && intersectTime >= carAheadIntersectTime)
                {
                    // That intersection time depends on whether or not the car ahead has caught up to a slow car though
                    // if the car ahead has already caught up to the one ahead of it
                    // we have to recalculate intersection time
                    s.pop();
                    continue;
                }
                else break;
            }
            answer[i] = intersectTime;
            s.push({(double) cars[i][0], (double) cars[i][1], intersectTime});
        }

        return answer;
    }

private:
    double calculateIntersectTime(vector<int>& carBehind, double carAheadPos, double carAheadSpeed)
    {
        // Each car can be represented by the line : CurPosition = Speed * Time + StartPos
        return (carBehind[0] - carAheadPos) / (carAheadSpeed - carBehind[1]);
    }
};

// Version 2 - Found a leetcode, this is essentially a refactored version of mine that runs faster
class Solution
{
public:
    vector<double> getCollisionTimes(vector<vector<int>> &A)
    {
        int n = A.size();
        vector<int> stack;
        vector<double> res(n, -1);
        for (int i = n - 1; i >= 0; --i)
        {
            int p = A[i][0], s = A[i][1];
            while (!stack.empty())
            {
                int j = stack.back(), p2 = A[j][0], s2 = A[j][1];
                if (s <= s2 || 1.0 * (p2 - p) / (s - s2) >= res[j] && res[j] > 0)
                    stack.pop_back();
                else
                    break;
            }
            if (!stack.empty())
                res[i] = 1.0 * (A[stack.back()][0] - p) / (s - A[stack.back()][1]);
            stack.push_back(i);
        }
        return res;
    }
}; 
