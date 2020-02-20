# 252. Meeting Rooms

## Description

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]` (si < ei), determine if a person could attend all meetings.

For example,
Given `[[0, 30],[5, 10],[15, 20]]`,
return false.

## Solution

### Sorting by the start time

1. Sorting by the start time
2. Iterate through, if the end time of the previous meeting is greater then the start time of current meeting, then it can't attend the current meeting.
