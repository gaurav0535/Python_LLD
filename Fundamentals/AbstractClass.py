from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def parameter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length*self.length

    def parameter(self):
        return 4*self.length




shape = Square(1)



#Here we are implementing the Abstract class behaviour using python 