// https://leetcode.com/problems/range-module/

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule* obj = new RangeModule();
 * obj->addRange(left,right);
 * bool param_2 = obj->queryRange(left,right);
 * obj->removeRange(left,right);
 */

// Version 1 - ordered_map that looks like {left1: right1, left2: right2, ...}
// Time complexity      O(n) for add or remove O(logn) for query
// Space complexity      O(n)
class RangeModule
{
public:
    RangeModule()
    {
    }

    void addRange(int left, int right)
    {
        // find where in the map the new interval is to be inserted (find iterator for right and left)
        auto l = intervals.upper_bound(left);
        auto r = intervals.upper_bound(right);
        // if the previous interval overlaps the interval to be added, we decrement iterator l
        // so the previous interval can be expanded to include this new one
        if (l != intervals.begin() && prev(l)->second >= left) --l;
        // check if the right of this new interval overlaps some of the next intervals
        if (l != r)
        {
            // make sure we are getting the correct bounds for the new interval, accounting for all the overlaps
            left = min(left, l->first);
            right = max(right, prev(r)->second);
            // erase and then ...
            intervals.erase(l, r);
        }
        // update
        intervals[left] = right;
    }

    bool queryRange(int left, int right)
    {
        // find the interval in which the query could lie in
        auto it = intervals.upper_bound(left);
        // if "it" is at begin means given interval has a smaller start than any existing
        // if prev->second is less than right our query interval overlaps an existing
        // in either case the query returns false
        if (it == intervals.begin() || prev(it)->second < right) return false;
        // else we are inside an interval
        return true;
    }

    void removeRange(int left, int right)
    {
        auto l = intervals.upper_bound(left);
        auto r = intervals.upper_bound(right);
        // same logic as from add
        if (l != intervals.begin() && prev(l)->second >= left) --l;
        // if l and r are the same, we are in between intervals and don't have to remove anything
        if (l == r) return;

        // if l->first is less than left or prev(r)->second is greater than right we are splitting this interval
        // save this information so that the old interval can be erased...
        int l1 = min(left, l->first);
        int r1 = max(right, prev(r)->second);
        intervals.erase(l, r);

        // ... and two new ones can be created
        if (l1 < left) intervals[l1] = left;
        if (r1 > right) intervals[right] = r1;
    }

private:
    map<int, int> intervals;
};
