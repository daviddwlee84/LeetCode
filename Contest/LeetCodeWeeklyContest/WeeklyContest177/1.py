from datetime import datetime

class Solution:
    """ https://stackoverflow.com/questions/8419564/difference-between-two-dates-in-python """
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.strptime(date1, r"%Y-%m-%d")
        d2 = datetime.strptime(date2, r"%Y-%m-%d")
        return abs((d2 - d1).days)
