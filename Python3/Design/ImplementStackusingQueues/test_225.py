from TwoQueue225 import MyStack as DoubleQueue

def test_DoubleQueue():
    obj = DoubleQueue()
    obj.push(3)
    obj.push(4)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
    assert param_2 == 4
    assert param_3 == 3
    assert param_4 == False