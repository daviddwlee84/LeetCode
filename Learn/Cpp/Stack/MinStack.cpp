
/**
 * Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
 * 
 * push(x) -- Push element x onto stack.
 * pop() -- Removes the element on top of the stack.
 * top() -- Get the top element.
 * getMin() -- Retrieve the minimum element in the stack.
 *  
 * 
 * Example:
 * 
 * MinStack minStack = new MinStack();
 * minStack.push(-2);
 * minStack.push(0);
 * minStack.push(-3);
 * minStack.getMin();   --> Returns -3.
 * minStack.pop();
 * minStack.top();      --> Returns 0.
 * minStack.getMin();   --> Returns -2.
 */

#include <iostream>
#include <vector>
#include <climits>

class MinStack
{
private:
    // store elements
    std::vector<int> data;
    // minimum value
    int min = INT_MAX;
    // minimum position
    int minPos = -1;

    void updateMin()
    {
        // find new min value
        min = INT_MAX;
        for (int i = 0; i < data.size(); i++)
        {
            if (data[i] < min)
            {
                // update
                min = data[i];
                minPos = i;
            }
        }
    }

public:
    /** initialize your data structure here. */
    MinStack()
    {
    }

    void push(int x)
    {
        data.push_back(x);
        if (x < min)
        {
            // update minimum
            min = x;
            minPos = data.size() - 1;
        }
    }

    void pop()
    {
        data.pop_back();
        if (minPos == data.size())
        {
            // if we pop the minimum one then we should update new minimum
            updateMin();
        }
    }

    int top()
    {
        return data.back();
    }

    int getMin()
    {
        return min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

void testcase1()
{
    MinStack *minStack = new MinStack();
    minStack->push(-2);
    minStack->push(0);
    minStack->push(-3);
    std::cout << minStack->getMin() << std::endl; // Returns - 3.
    minStack->pop();
    std::cout << minStack->top() << std::endl;    // Returns 0.
    std::cout << minStack->getMin() << std::endl; // Returns - 2.
}

int main()
{
    testcase1();
}

/**
 * Runtime: 24 ms, faster than 98.27% of C++ online submissions for Min Stack.
 * Memory Usage: 16.9 MB, less than 87.27% of C++ online submissions for Min Stack.
 */
