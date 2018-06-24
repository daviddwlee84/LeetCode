from TwoStack232 import MyQueue as DoubleStack

def test_DoubleStack():
    obj = DoubleStack()
    obj.push(1)
    obj.push(2)
    assert obj.pop() == 1
    assert obj.peek() == 2
    assert obj.empty() == False
