class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def affiche(self):
        return (self.x, self.y, self.z)
       
my_point = Point3D(1,2,3)
t=my_point.affiche()
print(t)
