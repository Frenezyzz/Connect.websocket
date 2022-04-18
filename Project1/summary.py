
from sympy import Q

from firstNumber import *
from lastNumber import *
from maxNumber import *
from minNumber import *
from quantityEvenNumbers import *
from quantityOddNumbers import *
from quantityPrimeNumbers import *
class Summary():
    summary = {}

    def __init__(self):
        
        self.summary = {
            'min_number': 0,
            'max_number':0,
            'first_number': 0,
            'last_number':0,
            'number_of_prime_numbers': 0,
            'number_of_even_numbers': 0,
            'number_of_odd_numbers': 0,
        }
    def setSummary(self,number):

        i = j =0
        
        a = MinNumber()
        b = MaxNumber()
        c = FirstNumber()
        d = LastNumber()

        e = QuantityPrimeNumbers()
        f = QuantityEvenNumbers()
        g = QuantityOddNumbers()
        
        
        
        instacesCalculate = [a,b,c,d]
        instacesCount = [e,f,g]
        keysCount = ['number_of_prime_numbers','number_of_even_numbers','number_of_odd_numbers']
        keysCalculate = ['min_number','max_number','first_number','last_number']

        for k in keysCalculate:
            self.summary[k] = instacesCalculate[i].calculate(self.summary[k],number)
            i +=1
        index = 0
        for k in keysCount:
            
            self.summary[k] = instacesCount[j].count(number,self.summary[k])
            j +=1
            
        return self.summary
           
