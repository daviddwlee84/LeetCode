from Naive155 import MinStack as naive
from Improve155 import MinStack as improve


def case1(constructor):
    minStack = constructor()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2

def case2(constructor):
    operation = ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
    value = [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
    answer = [None,None,None,None,2147483647,None,2147483646,None,2147483646,None,None,2147483647,2147483647,None,-2147483648,-2147483648,None,2147483647]
    for op, v, ans in zip(operation, value, answer):
        if op == 'MinStack':
            minStack = constructor()
        elif op == 'push':
            assert minStack.push(v[0]) == ans
        elif op == 'top':
            assert minStack.top() == ans
        elif op == 'getMin':
            assert minStack.getMin() == ans
        elif op == 'pop':
            assert minStack.pop() == ans
    

def test_naive():
    case1(naive)
    case2(naive)

def test_improve():
    case1(improve)
    case2(improve)
