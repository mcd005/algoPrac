// https://leetcode.com/problems/my-calendar-i/

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */

// Version 1 - Use a map that looks like {start: end}
// Time complexity      O(nlogm)
// Space complexity     O(m)
// For a n queries on a calendar of m booked events
class MyCalendar
{
public:
    MyCalendar()
    {
    }

    bool book(int start, int end)
    {
        if (isValidTimeSlot(start, end))
        {
            addEvent(start, end);
            return true;
        }
        return false;
    }

private:
    bool isValidTimeSlot(int start, int end)
    {
        if (eventTimes.empty()) return true;
        // Upper bound will find where the new event could be placed in the calendar
        auto s = eventTimes.upper_bound(start);
        // Two checks:
        //      Does the last event end before the one to be added (don't need to check if this if the event to be added is going to be the first)
        //      Does the event to be added overrun to next event already in the calendar?
        //          In the special case where start is greater than start of all current booked events
        //          then s will point to the last event. In which we need to check if the last event will overrun into the event to be added
        return ((s == eventTimes.begin() || prev(s)->second <= start) && (s->first >= end || s == eventTimes.end() && s->second <= start));
    }

    void addEvent(int start, int end)
    {
        eventTimes[start] = end;
    }

    map<int, int> eventTimes;
};
