
import unittest
import random
import firstNumber
import lastNumber
import maxNumber
import minNumber
import quantityEvenNumbers
import quantityOddNumbers
import quantityPrimeNumbers


import sympy
class Test_Number_Minimo(unittest.TestCase):
     

    def test_minimo(self):
        valuesTest = [0,10,5,80,30,10,0]
        valuesTest2 = [10,5,80,30,10,0,0]
        j = 0
        first_Number = 0
        c = firstNumber.FirstNumber()
        
        for i in valuesTest:
            if valuesTest2[j-1] != i and valuesTest2[j] == 0:
                first_Number = i
            c.calculate(valuesTest2[j-1],i)
            j +=1
           
        
        self.assertEqual(c.calculate(valuesTest2[j-1],i), first_Number)

class Test_Number_Maximo(unittest.TestCase):
     

    def maxNumber(self):
        
        number_maximo = 0
        c = maxNumber.MaxNumber()
        for i in range(5):
            x = random.randint(1,20)

            if x > number_maximo:
                number_maximo = x

            c.calculate(number_maximo,x)
            
        self.assertEqual(c.calculate(number_maximo,x), number_maximo)

class TestLastNumber(unittest.TestCase):
    def testingLastNumber(self):
        last_Number = 0
        valuesTest = [0,10,5,80,30,10,0]
        valuesTest2 = [10,5,80,30,10,0,0]
        c = lastNumber.LastNumber()
        j = 0
        for i in valuesTest:
            last_Number = i
            c.calculate(valuesTest2[j-1],i)
            j +=1
        
        self.assertEqual(c.calculate(valuesTest2[j-1],i), last_Number)
            
class TestMinNumber(unittest.TestCase):
    def testingMinNumber(self):
        min_Number = 99999999
        c = minNumber.MinNumber()
        for i in range(5):
            x = random.randint(1,20)

            if x < min_Number:
                min_Number = x

            c.calculate(min_Number,x)
            
        self.assertEqual(c.calculate(min_Number,x), min_Number)

class TestQuantityEvenNumber(unittest.TestCase):
    def testingQuantityEvenNumber(self):
        valuesTest = [0,10,5,80,30,10,0]
        countEven = 0
        c = quantityEvenNumbers.QuantityEvenNumbers()
        for i in valuesTest:
            if i % 2 == 0:       
                countEven += 1
            c.count(i,countEven)
        
        self.assertEqual(c.count(1,countEven), countEven)

class TestQuantityOddNumber(unittest.TestCase):
    def testingQuantityOddNumber(self):
        valuesTest = [0,10,5,3,30,7,0]
        countOdd = 0
        c = quantityOddNumbers.QuantityOddNumbers()
        for i in valuesTest:
            if i % 2 != 0:       
                countOdd += 1
            c.count(i,countOdd)
        
        self.assertEqual(c.count(2,countOdd), countOdd)
class TestQuantityPrimeNumber(unittest.TestCase):
    def testingQuantityPrimeNumber(self):
        valuesTest = [0,10,5,3,30,7,0]
        countPrime = 0
        c = quantityPrimeNumbers.QuantityPrimeNumbers()
        for i in valuesTest:
            if sympy.isprime(i):       
                countPrime += 1
            c.count(i,countPrime)
        
        self.assertEqual(c.count(0,countPrime), countPrime)
if __name__ == "__main__":
    unittest.main()
        
