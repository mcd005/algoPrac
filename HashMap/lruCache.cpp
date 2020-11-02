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

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */