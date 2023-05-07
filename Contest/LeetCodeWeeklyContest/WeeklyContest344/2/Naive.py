from collections import defaultdict


class FrequencyTracker:
    def __init__(self):
        self.data = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        if self.data[number] in self.freq:
            self.freq[self.data[number]] -= 1
            if self.freq[self.data[number]] == 0:
                del self.freq[self.data[number]]
        self.data[number] += 1
        self.freq[self.data[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number not in self.data:
            return

        if self.data[number] in self.freq:
            self.freq[self.data[number]] -= 1
            if self.freq[self.data[number]] == 0:
                del self.freq[self.data[number]]

        self.data[number] -= 1
        if self.data[number] == 0:
            del self.data[number]
        else:
            self.freq[self.data[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        # O(n) will TLE
        return frequency in self.freq


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
