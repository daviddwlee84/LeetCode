import TreeNode as tn
from Recursive144 import Solution as recursive
from Iterative144 import Solution as iterative

testcase = []
testcase.append(tn.stringToTreeNode("[1,null,2,3]"))
testcase.append(tn.stringToTreeNode("[]"))

preorderAns = []
preorderAns.append([1, 2, 3])
preorderAns.append([])

def test_recursive_preorder():
    for num, case in enumerate(testcase):
        assert recursive().preorderTraversal(case) == preorderAns[num]
    
def test_iterative_preorder():
    for num, case in enumerate(testcase):
        assert iterative().preorderTraversal(case) == preorderAns[num]