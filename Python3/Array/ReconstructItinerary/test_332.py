from Naive332 import Solution as naive
from EulerianPath332 import Solution as eulerian_path
from DFS332 import Solution as DFS

testcase = [
    ([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], [
     "LHR", "SFO"]], ["JFK", "MUC", "LHR", "SFO", "SJC"]),
    ([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"],
      ["ATL", "SFO"]], ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
    ([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]],
     ["JFK", "NRT", "JFK", "KUL"]),
    ([["JFK", "ATL"], ["ATL", "JFK"]],
     ["JFK", "ATL", "JFK"]),
    ([["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], ["ANU", "EZE"], ["TIA", "ANU"], ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]],
     ["JFK", "ANU", "EZE", "AXA", "TIA", "ANU", "JFK", "TIA", "ANU", "TIA", "JFK"])
]


def test_naive():
    for tickets, ans in testcase:
        assert naive().findItinerary(tickets) == ans


def test_eulerian_path():
    for tickets, ans in testcase:
        assert eulerian_path().findItinerary(tickets) == ans


def test_DFS():
    for tickets, ans in testcase:
        assert DFS().findItinerary(tickets) == ans
