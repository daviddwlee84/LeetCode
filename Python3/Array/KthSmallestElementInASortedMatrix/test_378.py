from Naive378 import Solution as naive
testcases = [
    ([[1,5,9],[10,11,13],[12,13,15]], 8, 13),
    ([[-5]], 1, -5),
    ([[1,2],[1,3]], 2, 1),
    ([[1,3,5],[6,7,12],[11,14,14]], 5, 7)
]

def test_naive():
    for matrix, k, ans in testcases:
        assert naive().kthSmallest(matrix, k) == ans, f'{matrix}, {k}'
