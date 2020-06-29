from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
        # vectors = set([airport for sublist in tickets for airport in sublist])
        self.edges = defaultdict(list)
        ends = set()
        ticket_left = set()
        for index, (start, to) in enumerate(tickets):
            ticket_left.add(index)
            ends.add(to)
            self.edges[start].append((to, index))

        # IMPORTANT:  All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

        # decide first airport
        # start = None
        # for airport in vectors:
        #     if airport not in ends:
        #         start = airport
        #         break

        start = "JFK"

        self.all_visit = []

        if start:
            self.findPossibleVisits([start], ticket_left.copy())
        # else:
        #     # try all start
        #     for start in self.edges.keys():
        #         self.findPossibleVisits([start], ticket_left.copy())

        return min(self.all_visit)

    def findPossibleVisits(self, curr_visit, ticket_left):
        if not ticket_left:
            self.all_visit.append(curr_visit)
            return

        curr_location = curr_visit[-1]
        if curr_location not in self.edges:
            return

        for next_location, index in self.edges[curr_location]:
            if index in ticket_left:
                self.findPossibleVisits(
                    curr_visit + [next_location], ticket_left - set([index]))

# TLE
# [["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]]
