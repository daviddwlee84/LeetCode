from Naive443 import Solution as Naive

testcases = (
    (["a", "a", "b", "b", "c", "c", "c"], 6, ["a", "2", "b", "2", "c", "3"]),
    (["a"], 1, ["a"]),
    (["a", "b", "b", "b", "b", "b", "b", "b", "b",
     "b", "b", "b", "b"], 4, ["a", "b", "1", "2"]),
)


def test_Naive():
    for chars, length, compressed in testcases:
        input_chars = chars.copy()
        assert Naive().compress(input_chars) == length
        assert input_chars == compressed
