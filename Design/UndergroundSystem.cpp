// https://leetcode.com/problems/design-underground-system/

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */

// Version 1 - Map for current journeys and map for each route
// Time complexity      O(1) for all ops
// Space complexity     O(N + M) for N peak concurrent journeys and M unique routes
class UndergroundSystem
{
public:
    UndergroundSystem()
    {
    }

    void checkIn(int id, string stationName, int t)
    {
        currentTravellers[id] = std::pair(stationName, t);
    }

    void checkOut(int id, string stationName, int t)
    {
        string startStation = currentTravellers[id].first;
        int duration = t - currentTravellers[id].second;
        currentTravellers.erase(id);
        string fromTo = startStation + "-" + stationName;
        routeInfo[fromTo].first += duration;
        ++routeInfo[fromTo].second;
    }

    double getAverageTime(string startStation, string endStation)
    {
        auto it = routeInfo.find(startStation + "-" + endStation);
        auto route = it->second;
        return (1.0 * route.first / route.second);
    }

private:
    unordered_map<int,pair<string, int>> currentTravellers; // id : {startStation, startTime}
    unordered_map<string,pair<int, int>> routeInfo; // from-to : {sum duration, num_trip}
};




// Version 2 - Found on LC. Map of maps for my equivalent of route info
class UndergroundSystem
{
private:
    // start -> dest -> number of trips, total distance
    unordered_map<string, unordered_map<string, pair<int, double>>> history;
    unordered_map<int, pair<string, int>> customerCheckIns;

public:
    UndergroundSystem()
    {
    }

    void checkIn(int id, string stationName, int t)
    {
        // uses the fact that a customer can only be checked into one place at a time.
        // time: O(1)
        // space: O(1)

        customerCheckIns[id].first = stationName;
        customerCheckIns[id].second = t;
    }

    void checkOut(int id, string stationName, int t)
    {
        // time: O(1)
        // space: O(N^2) where N is the number of stations visited
        pair<string, int> lastCheckIn = customerCheckIns[id];
        history[lastCheckIn.first][stationName].first++;
        history[lastCheckIn.first][stationName].second += (double)t - lastCheckIn.second;
    }

    double getAverageTime(string startStation, string endStation)
    {
        // time: O(1)
        // space: O(1)
        auto stationHistory = history[startStation][endStation];
        return stationHistory.second / stationHistory.first;
    }
};