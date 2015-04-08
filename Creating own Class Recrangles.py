#Rectangles.py class is placed in the same location that this program 
#is calling to use... like both on desktop or both in same folder
from Rectangles import Rectangles
def main():
    
    rect1 = Rectangles(4, 40)
    print('Wength: ',rect1.getWidth())
    print('Height: ',rect1.getHeight())
    print('Area for the Rectangle is: ', rect1.getArea())
    print('Perimeter for the Rectangle is: ', rect1.getPerimeter())


    #seperate the answers
    print('\n\n')
    
    rect2 = Rectangles(3.5,35.7)
    print('Wength: ',rect2.getWidth())
    print('Height: ',rect2.getHeight())
    print('Area for the Rectangle is: ', round(rect2.getArea(),2))
    print('Perimeter for the Rectangle is: ', round(rect2.getPerimeter(),2))
    
main()

/////////////////////////////////////////////////////////////////////////////
# This is a seperate python program, keep it in same place as the main program
class Rectangles:
    def __init__(self, Width = 1, Height = 2):
        self.__Width = Width
        self.__Height = Height
        
    def getWidth(self):
        return self.__Width
    def getHeight(self):
        return self.__Height
    def setWidth(self, Width):
        self.__Width = Width
    def setHeight(self, Height):
        self.__Height = Height
    def getArea(self):
        Area = self.__Width*self.__Height
        return Area
    def getPerimeter(self):
        Perimeter = 2*(self.__Width + self.__Height)
        return Perimeter

