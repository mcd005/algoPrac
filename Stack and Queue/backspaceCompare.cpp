class Solution {
public:
    bool backspaceCompare(string S, string T) {
        stack<char> sStack, tStack;
        sStack = stackify(S);
        tStack = stackify(T);
        
        
        if (sStack.size() != tStack.size()) return false;
        
        while (!sStack.empty()){
            if (sStack.top() != tStack.top()){
                return false;
            }
            sStack.pop();
            tStack.pop();
        }
        
        return true;
    }
    
    stack<char> stackify(string X){
        stack<char> stck;
        
        for (int i = 0; i < X.size(); i++){
            if (X[i] == '#'){
                if (!stck.empty()){
                    stck.pop();
                }
            }
            else{
                stck.push(X[i]);
            }
        }
        
        return stck;
    }
};