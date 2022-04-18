from calculatorStrategy import *
class MaxNumber(CalculatorStrategy):

    
    def calculate(self, summaryPervious,number):
        
        if number > summaryPervious:
            return number
        else:
            return summaryPervious

