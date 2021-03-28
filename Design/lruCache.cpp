// https://leetcode.com/problems/lru-cache/

/*
We'll use a doubly linked list as a queue to keep track of when things were used recently
    Head of queue is used most recently and the tail/back is the LRU

We'll use a map so we can look up the postion of each key in that queue in O(1)

Time complexity         O(1) for all operations
Space complexity        O(capacity)
*/

// Version 4 - Attempted clean code version
class LRUCache {
public:
    LRUCache(int capacity) :
    cacheCapacity(capacity)
    {}
    
    int get(int key) {
        auto keyMapIterator = keyQPositions.find(key);
        if (isKeyInCache(keyMapIterator))
        {
            auto keyPosInQ = keyMapIterator->second;
            setKeyToMRU(keyPosInQ);
            return getKeyValue(keyPosInQ);
        }
        return -1;
    }
    
    void put(int key, int value) {
        auto keyMapIterator = keyQPositions.find(key);
        if (isKeyInCache(keyMapIterator))
        {
            auto keyPosInQ = keyMapIterator->second;
            setKeyToMRU(keyPosInQ);
            setKeyValue(keyPosInQ, value);
        }
        else 
        {
            if (!isCacheFull())
            {
                addNewKeyVal(key, value);
            }
            else
            {
                evictLRUkey();
                addNewKeyVal(key, value);
            }
        }
    }
private:
    int cacheCapacity;
    // First is key, second is val. Back of queue is the least recently used key
    list<pair<int, int>> recencyQ;; 
    std::unordered_map<int, std::list<pair<int,int>>::iterator> keyQPositions;

    bool isKeyInCache(std::unordered_map<int, std::list<pair<int,int>>::iterator>::iterator keyMapIterator)
    {
        return keyMapIterator != keyQPositions.end();
    }

    void setKeyToMRU(std::list<pair<int,int>>::iterator keyCurrentQposition)
    {
        recencyQ.splice(recencyQ.begin(), recencyQ, keyCurrentQposition);
    }

    int getKeyValue(std::list<pair<int,int>>::iterator keyQPos)
    {
        return keyQPos->second;
    }

    void setKeyValue(std::list<pair<int,int>>::iterator keyQPos, int val)
    {
        keyQPos->second = val;
    }

    bool isCacheFull()
    {
        return recencyQ.size() >= cacheCapacity;
    }

    void addNewKeyVal(int k, int v)
    {
        recencyQ.emplace_front(k, v);
        keyQPositions[k] = recencyQ.begin();
    }

    void evictLRUkey()
    {
        auto lruKey = recencyQ.back();
        keyQPositions.erase(lruKey.first);
        recencyQ.pop_back();
    }
};



// Version 3 - Using STL implementations of list
// Use a list as q queue of recency 
class LRUCache {
public:
    LRUCache(int capacity) :
    cacheCapacity(capacity) {}
    
    int get(int key) {
        auto keyPos = keyQPositions.find(key);
        if (keyPos != keyQPositions.end())
        {
            recencyQ.splice(recencyQ.begin(), recencyQ, keyPos->second);
            return keyPos->second->second;
        }
        return -1;
    }
    
    void put(int key, int value) {
        auto keyPos = keyQPositions.find(key);
        if (keyPos != keyQPositions.end())
        {
            recencyQ.splice(recencyQ.begin(), recencyQ, keyPos->second);
            keyPos->second->second = value;
        }
        else 
        {
            if (keyQPositions.size() < cacheCapacity)
            {
                recencyQ.emplace_front(key, value);
                keyQPositions[key] = recencyQ.begin();
            }
            else
            {
                auto lruKey = recencyQ.back();
                keyQPositions.erase(lruKey.first);
                recencyQ.pop_back();
                recencyQ.emplace_front(key, value);
                keyQPositions[key] = recencyQ.begin();
            }
        }
    }
private:
    int cacheCapacity;
    list<pair<int, int>> recencyQ;; 
    std::unordered_map<int, std::list<pair<int,int>>::iterator> keyQPositions;
};



//Version 2 - Using own implementation of doubly linked list 
class LRUCache {
public:
    struct ListNode
    {
        int val, key;
        ListNode *next, *pre;
        ListNode(int k, int v):val(v),key(k), next(nullptr), pre(nullptr){}
    };

    LRUCache(int capacity) {
        size = capacity;
        head = new ListNode(0,0);
        tail = new ListNode(0,0);
        head->next = tail;
        tail->pre = head;
    }
    
    int get(int key) {
        if(store.find(key) == store.end()){
            return -1;
        }
        ListNode *n = store[key];
        remove(n);
        insert(n);
        return n->val;
    }
    
    void put(int key, int value) {
        ListNode *n = nullptr;
        if(store.find(key) == store.end()){
            n = new ListNode(key, value);          
            if(store.size() == size){
                ListNode *toDelete = tail->pre;
                store.erase(toDelete->key);
                toDelete->pre->next = tail;
                tail->pre = toDelete->pre;
                delete toDelete;
            }
            store[key] = n;
        }else{
            n = store[key];
            n->val = value;
            remove(n);
        }
        insert(n);
    }
private:
    int size;
    ListNode *head, *tail;
    unordered_map<int, ListNode*> store;
    void insert(ListNode *n){
        n->next = head->next;
        n->pre = head;
        head->next = n;
        n->next->pre = n;
    }
    void remove(ListNode *n){
        n->pre->next = n->next;
        n->next->pre = n->pre;
    }
};



// Version 1 - Naive, tracking time
class LRUCache {
public:
    int maxSize, time = 0;
    unordered_map<int, int> cache, ages;

    LRUCache(int capacity) {
         maxSize = capacity;
    }
    
    int get(int key) {
        // printCache();
        time++;
        if (cache.find(key) != cache.end()){
            ages[key] = time;
            return cache[key];
        }
        else{
            return -1;
        }
    }
    
    void put(int key, int value) {
        time++;
        if (cache.size() >= maxSize && cache.find(key) == cache.end()){
            int lru = findLRU();
            cache.erase(lru);
            ages.erase(lru)  ;  
        }
        cache[key] = value;
        ages[key] = time;
    }
    
    int findLRU(){
        int lruKey = ages.begin()->first;
        int earliest = ages.begin()->second;
    
        for (unordered_map<int, int>::iterator it = ages.begin(); it != ages.end(); it++){
            if (it->second < earliest){
                lruKey = it->first;
                earliest = it->second;
            }
        }
        
        return lruKey;
    }
    
    // void printCache(){
    //     for (unordered_map<int, int>::iterator it = cache.begin(); it != cache.end(); it++){
    //         cout << it->first << " : " << it->second << endl;
    //     }
    //     cout << "\n" << endl;
    // }
};