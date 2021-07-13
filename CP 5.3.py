##Write a Python  class named Circle constructed by its center O and radius r.
##Define two methods area and perimeter which will compute the area and the perimeter of the circle, and isInside() method of the class which allows to test whether a point
##A(x, y) belongs to the circle C(O, r) or not.

class circle:
    def __init__(self,xycoord_center,r):
        self.xycoord_center=xycoord_center
        self.r=r
    def area(self):
        self.area=(self.r**2)*pi
        return self.area
    def perimeter(self):
        self.perimeter=self.r*2*pi
        return self.perimeter
    def isinside(self,point_coord):
        a=self.a=self.xycoord_center[0]
        b=self.b=self.xycoord_center[1]
        x=point_coord[0]
        y=point_coord[1]
        distance_center_point=((x-a)**2+(y-b)**2)**0.5
        if distance_center_point<self.r:
            return 'point inside'
        elif distance_center_point==self.r:
            return 'point on the circumference'
        else:
            return 'point outside'
        

circle=circle([10,5],5)
print(circle.isinside([3,9]))
