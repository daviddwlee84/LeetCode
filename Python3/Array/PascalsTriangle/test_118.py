from Naive118 import Solution as naive

PascalsTriangle = [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

def test_naive():
    for numRows in range(6):
        assert naive().generate(numRows) == PascalsTriangle[:numRows]
