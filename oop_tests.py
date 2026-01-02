class SimpleObj:
    def __init__(self, id):
        self.id = id
    
    def get_id(self):
        return self.id

obj = SimpleObj(22)
print("Id: ", obj.get_id(), "\n")

# ----

class Quadrilateral:
    def __init__(self, s1, s2, s3, s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
    
    def __repr__(self):
        return f"Quad:({self.s1}, {self.s2}, {self.s3}, {self.s4})"
    
quad = Quadrilateral(4,4,4,4)
print(quad, "\n")

# ----

class Rectangle(Quadrilateral):
    def __init__(self, s1, s2):
        super().__init__(s1, s2, s1, s2)

    def __repr__(self):
        return f"Rect:({self.s1}, {self.s2}, {self.s1}, {self.s2})"

    def area(self):
        return self.s1 * self.s2
    
    def perimeter(self):
        return 2 * (self.s1 + self.s2)

rect = Rectangle(2,4)
print(rect)
print(rect.area())
print(rect.perimeter(), "\n")

# ----

class Square(Rectangle):
    def __init__(self, s1, s2):
        super().__init__(s1, s2)

    def __repr__(self):
        return f"Squr:({self.s1}, {self.s2}, {self.s1}, {self.s2})"

squr = Square(2,4)
print(squr)
print(squr.area())
print(squr.perimeter(), "\n")
