// https://leetcode.com/problems/logger-rate-limiter/

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */

// Version 2 - Clean code version
class Logger {
public:
    /** Initialize your data structure here. */
    Logger() {
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        if (!messageIsUnique(message) && messageIsTooEarly(timestamp, message))
        {
            return false;
        }
        setNextAllowedTimestamp(timestamp, message);
        return true;
     }

    bool messageIsUnique(string messsage)
    {
        return nextAllowedTimestamps.find(message) == nextAllowedTimestamps.end();
    } 

    bool messageIsTooEarly(int timestamp, string message)
    {
        return timestamp < nextAllowedTimestamps[message];
    }

    void setNextAllowedTimestamp(int timestamp, string message)
    {
        nextAllowedTimestamps[message] = timestamp + 10;
    }
    

private:
    std::unordered_map<string, int> nextAllowedTimestamps; 
};

// Version 1 - Quick implementation
class Logger {
public:
    /** Initialize your data structure here. */
    Logger() {
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        if (messageMap.find(message) != messageMap.end())
        {
            if (timestamp >= messageMap[message])
            {
                messageMap[message] = timestamp + 10;
                return true;
            } 
            return false;
        }
        messageMap[message] = timestamp + 10;
        return true;
    }
    

private:
    std::unordered_map<string, int> messageMap; 
};
