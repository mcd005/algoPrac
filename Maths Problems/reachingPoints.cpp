// https://leetcode.com/problems/reaching-points/

// Essentially we are subtracting tx from ty or ty from tx until we reach sx and sy
// Doing this naively, however, will be to slow so we take a couple of shortcuts:
//      1) Rather than doing "tx = tx - ty" we do "tx = tx % ty" which is like doing subtraction multiple times
//      2) Lets say for argument sake we have subtracted tx enough times that tx == sx.
//         Lets also say that ty > sy is still true. All we can do is now is subtract tx from ty
//         So if there isn't a whole number of tx's in ty - sy then we know if will be impossible to reach (tx == sx, ty == sy)
//         Hence we check (ty - sy) % sx == 0 and vice versa if ty == sx

// In terms of a recursive tree
// #1 allows the tree to be shorter/less deep
// #2 trims branches that won't yield a solution

// Version 3 - Iterative (more readable)
// Time complexity      O(log(max(tx, ty)))
// Space complexity     O(1)
class Solution {
public:
      bool reachingPoints(int sx, int sy, int tx, int ty) {
        // tx < ty is so that we don't get stuck in an infinite loop
        while (sx < tx && sy < ty) {
            if (tx < ty) ty %= tx;
            else tx %= ty;
        }
        return sx == tx && sy <= ty && (ty - sy) % sx == 0 ||
               sy == ty && sx <= tx && (tx - sx) % sy == 0;
    }
};

// Version 2 - Iterative (compact)
class Solution {
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        while (sx < tx && sy < ty) tx < ty ? ty %= tx : tx %= ty;
        return sx == tx && sy <= ty && (ty - sy) % sx == 0 || sy == ty && sx <= tx && (tx - sx) % sy == 0;
    }
};

// Version 1 - Recursive
// Time complexity      O(log(max(tx, ty)))
// Space complexity     O(log(max(tx, ty)))
class Solution {
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        if (tx < sx || ty < sy) return false;
        if (tx == sx && ty == sy) return true;
        if (tx == sx) return (ty - sy) % tx == 0;
        if (ty == sy) return (tx - sx) % ty == 0;
        return (tx > ty) ? reachingPoints(sx, sy, tx % ty, ty) : reachingPoints(sx, sy, tx, ty % tx);
    }
};