from calculatorStrategy import *
class MinNumber(CalculatorStrategy):
    
    def calculate(self,summaryPervious,number):

        if number < summaryPervious or summaryPervious == 0:
            
            return number
        else:
            return summaryPervious

