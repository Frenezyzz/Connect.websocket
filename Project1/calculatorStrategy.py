
from abc import ABC,abstractmethod


class CalculatorStrategy(ABC):

    @abstractmethod 
    def calculate(self,summaryPervious,number):
        pass


