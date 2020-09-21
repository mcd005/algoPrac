/*
https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/

Basically had to implement a queue with two stacks
Used an "oldest_on_top" stack to return values for front or to carry out q.dequeue
Used a "newest_on_top" stack so new values could be enqueued

If the "oldest_on_top" stack was empty at the time of a .front() or a .pop() then it could be populated by emptying the "newest_on_top" stack onto it (so the top of "newest" is now the bottom of "oldest")

At face value this "flipping stacks" may appear to make dequeues cost O(n) (where n is the number of elements on the "newest" stack)
However amortised time analysis can be applied

Say in the worst case we enqueue N elements but then call q.front()
Although we would have to move n elements from one stack to the other, the dequeue opeartion for the next n - 1 elements would happen in constant time
This means we are perfoming N operations over N elements, hence average time complexity is O(1)
*/

class MyQueue {
    public:
        stack<int> stack_newest_on_top, stack_oldest_on_top;   
        void push(int x) {
            stack_newest_on_top.push(x);
        }

        void pop() {
            if (stack_oldest_on_top.empty()){
                flipStacks();
            }
            stack_oldest_on_top.pop();
        }

        int front() {
            if (stack_oldest_on_top.empty()){
                flipStacks();
            }
            return stack_oldest_on_top.top();
        }

        void flipStacks() {
            while (!stack_newest_on_top.empty()){
                stack_oldest_on_top.push(stack_newest_on_top.top());
                stack_newest_on_top.pop();
            }
        }
};

int main() {
    MyQueue q1;
    int q, type, x;
    cin >> q;
    
    for(int i = 0; i < q; i++) {
        cin >> type;
        if(type == 1) {
            cin >> x;
            q1.push(x);
        }
        else if(type == 2) {
            q1.pop();
        }
        else cout << q1.front() << endl;
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}