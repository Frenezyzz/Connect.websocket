from abc import ABC,abstractmethod

class CountStrategy(ABC):
    @abstractmethod 
    def count(self,number,currentCount):
        pass