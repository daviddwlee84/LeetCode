from BinaryTree.SerializeAndDeserializeBinaryTree.Naive297 import Codec as naive

testcase = [
    '[1,2,3,null,null,4,null,null,5]',
    '[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]',
    "[]",
    "[1,2,3,null,null,4,5]",
    "[-1,0,1]",
    "[5,2,3,null,null,2,4,3,1]"
]

def test_naive():
    codec = naive()
    for string in testcase:
        assert codec.serialize(codec.deserialize(string)) == string
