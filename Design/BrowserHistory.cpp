// https://leetcode.com/problems/design-browser-history/submissions/

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */

// Version 1 - 2 stacks
// Time complexity          O(n)
// Space complexity         O(n)
class BrowserHistory
{
public:
    BrowserHistory(string homepage) : currentPage(homepage)
    {
    }

    void visit(string url)
    {
        prevPages.push(currentPage);
        currentPage = url;
        clearNextPages();
    }

    string back(int steps)
    {
        while (!prevPages.empty() && steps--)
        {
            nextPages.push(currentPage);
            currentPage = prevPages.top();
            prevPages.pop();
        }
        return currentPage;
    }

    string forward(int steps)
    {
        while (!nextPages.empty() && steps--)
        {
            prevPages.push(currentPage);
            currentPage = nextPages.top();
            nextPages.pop();
        }
        return currentPage;
    }

    void clearNextPages()
    {
        while (!nextPages.empty())
        {
            nextPages.pop();
        }
    }

private:
    string currentPage;
    stack<string> prevPages, nextPages;
};



// Version 2 - Using a vector
// Improve TC excpet for visit
class BrowserHistory
{
public:
    BrowserHistory(string homepage) : mCurIndex(0)
    {
        mHistory.push_back(homepage);
    }

    void visit(string url)
    {
        int n = mHistory.size();
        if (mCurIndex < n - 1)
            mHistory.erase(mHistory.begin() + mCurIndex + 1, mHistory.end());

        mHistory.push_back(url);
        mCurIndex = mHistory.size() - 1;
    }

    string back(int steps)
    {
        if (mHistory.empty())
            return "";

        if (mCurIndex - steps > 0)
            mCurIndex -= steps;
        else
            mCurIndex = 0;

        return mHistory[mCurIndex];
    }

    string forward(int steps)
    {
        if (mHistory.empty())
            return "";

        int n = mHistory.size();
        if (mCurIndex + steps > n - 1)
            mCurIndex = n - 1;
        else
            mCurIndex += steps;

        return mHistory[mCurIndex];
    }

private:
    vector<string> mHistory;
    int mCurIndex;
};


// Version 3 - Vector with slightly different logic
// Improve TC excpet for visit
class BrowserHistory
{
public:
    // record the visit history
    vector<string> cache_;
    // maximum step we can back
    int back_ = 0;
    // current index
    int cur_ = 0;
    // maximum step we can forward
    int forward_ = 0;
    BrowserHistory(string homepage)
    {
        cache_.push_back(homepage);
    }

    void visit(string url)
    {
        // put new url in next position
        if (cache_.size() == cur_ + 1)
        {
            cache_.push_back(url);
        }
        else
        {
            cache_[cur_ + 1] = url;
        }
        // clean forward history
        forward_ = 0;
        // add one more back and update current index
        back_ += 1;
        cur_ += 1;
    }

    string back(int steps)
    {
        auto step = std::min(back_, steps);
        back_ -= step;
        cur_ -= step;
        forward_ += step;
        return cache_[cur_];
    }

    string forward(int steps)
    {
        auto step = std::min(forward_, steps);
        forward_ -= step;
        cur_ += step;
        back_ += step;
        return cache_[cur_];
    }
};