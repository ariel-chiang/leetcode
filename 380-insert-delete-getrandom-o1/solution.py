import random

class RandomizedSet:

    def __init__(self):
        # record the index of each value with a dict
        self.valIdx = dict()
        self.values = list()

    def insert(self, val: int) -> bool:
        if val in self.valIdx:
            return False
        else:
            self.valIdx[val] = len(self.values)
            self.values.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.valIdx:
            # always remove the last element of the list
            # substitute the target value with the last element's value
            if self.valIdx[val] != len(self.values)-1:
                self.values[self.valIdx[val]] = self.values[-1]
                self.valIdx[self.values[-1]] = self.valIdx[val]
            self.values.pop()
            del self.valIdx[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()