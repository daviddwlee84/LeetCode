from typing import List
from Backtracking842 import Solution as Backtracking

testcases = [
    ("1101111", True),
    ("112358130", False),
    ("0123", False),
    ("0000", True),
    ("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511", False),
    ("3611537383985343591834441270352104793375145479938855071433500231900737525076071514982402115895535257195564161509167334647108949738176284385285234123461518508746752631120827113919550237703163294909", False),
]


def is_valid_fib_seq(sequence: List[int]) -> bool:
    for i in range(len(sequence) - 2):
        if sequence[i] + sequence[i + 1] != sequence[i + 2]:
            return False
    return True


def len_is_equal(num: str, sequence: List[int]) -> bool:
    return num == ''.join(str(n) for n in sequence)


def test_backtracking():
    for num, should_exist_answer in testcases:
        candidate = Backtracking().splitIntoFibonacci(num)
        if not should_exist_answer:
            assert candidate == []
        else:
            assert len_is_equal(num, candidate)
        assert is_valid_fib_seq(candidate)
