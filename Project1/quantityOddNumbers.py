from countStrategy import *
class QuantityOddNumbers(CountStrategy):
    def count(self, number,currentCount):
        if number % 2 != 0:       
            return currentCount + 1
        else:
            return currentCount