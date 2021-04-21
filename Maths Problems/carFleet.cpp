// https://leetcode.com/problems/car-fleet//

/* 
Each car can be represented by the line: CurPosition = Speed * Time + StartPos

We want to find if lines intersect and if their intersection occurs before target
But on the intersection of two lines they both take the speed of the slower vehicle (i.e. the lines merge into the less steep one)

We need to start with the car at the front and ask: Is the car behind going to catch up?
If it is we treat them both as the slower car, else we move on.
We repeat the process until there is a car behind that won't catch up

Algo:
    We zip the positions and speeds
    Then we sort by position so that the car closest to the target is first
    We treat the line of cars as a stack
    We pop the front one off and call it currentFleetLead
    While there are cars in the stack. If the top car will intersect with current front before the destination, we pop it off and decrement fleet count
        Intersection will just involve solving the equation and distance has to be less than target
    Otherwise we treat it as a new fleet and set it to current fleet lead
    At the end we return the number of fleets

Clean code version use a car struct
*/

// Version 1
// Time complexity      O(nlogn)
// Space complexity     O(n)
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
       int n = position.size();
       if (n == 0 || n == 1) return n;

       priority_queue<pair<float, float>> cars;
       for (int i = 0; i < n; ++i)
       {
           cars.push({(float) position[i], (float) speed[i]});
       }

       int numFleets = n;
       pair<float, float> currentFleetLead = cars.top();
       cars.pop();

       while (!cars.empty())
       {
           if (willCatchFleetLead(currentFleetLead, cars.top(), target)) --numFleets;
           else currentFleetLead = cars.top();
           cars.pop();
       }

       return numFleets;
    }

    bool willCatchFleetLead(pair<float, float> &leadCar, const pair<float, float> &pursuingCar, int target)
    {
        if (leadCar.second >= pursuingCar.second) return false;
        float intersectionTime = (leadCar.first - pursuingCar.first)/(pursuingCar.second - leadCar.second);
        float intersectionPoint = leadCar.second * intersectionTime + leadCar.first;
        if (intersectionPoint <= target) return true;
        return false;
    }
};

// Version 2 - Similar logic with simpler maths
// Time complexity      O(nlogn)
// Space complexity     O(n)
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        if(position.empty()) return 0;
        
        vector<pair<float,float>> ps(position.size());
        for(int i = 0; i < position.size(); ++i)
            ps[i] = {position[i],speed[i]};
        
        sort(ps.begin(), ps.end(), [](auto& l, auto& r){return l.first > r.first;});
        
        int res = 0;
        float fleet_leading_car_t = 0;
        for(int i = 0; i < ps.size(); ++i){
            //i.e. how long does it take the car to get to target
            float t = (target - ps[i].first) / ps[i].second;
            if(t > fleet_leading_car_t){
                fleet_leading_car_t = t;
                ++res;
            }
        }
        
        return res;
    }
};