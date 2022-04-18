
import sympy

from countStrategy import *
class QuantityPrimeNumbers(CountStrategy):
    
    def count(self, number,currentCount):
        if sympy.isprime(number):           
            return currentCount + 1
        else:
            return currentCount
