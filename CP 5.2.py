class rectangle :
    
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def perimeter(self):
        perimeter = 2*(self.width+self.length)
        return perimeter

    def area(self):
        area = self.width * self.length
        return area
my_rectangle = rectangle(2,3)

print("perimeter:" , my_rectangle.perimeter())
print("area:" , my_rectangle.area())
