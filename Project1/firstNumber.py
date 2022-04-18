

from calculatorStrategy import *

class FirstNumber(CalculatorStrategy):

    def calculate(self, summaryPervious,number):
        if summaryPervious != number and summaryPervious == 0:
            return number
        else:
            return summaryPervious

