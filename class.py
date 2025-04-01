class Human:
    def __init__(self, n, ag_e):
        self.name=n
        self.age=ag_e

    def walk(self):
        print(self.name, 'walk')

class Rectangle:
    def __init__(self, st1, st2):
        self.a=st1
        self.b=st2

    def S(self):
        return self.a*self.b




class Sphere:
    def __init__(self, name, r):
        self.Name=name
        self.radius=r

    def S(self):
        return 3.14*(self.radius**2)

    def D(self):
        return 2*3.14*self.radius


sh=Sphere('jall',17)
print(sh.S())
print(sh.D())


# d=Rectangle(24,3)
# print(d.S())
#
# s=Human('Jake', 20)
# f=Human('Alice', 38)
# f.walk()
# print(type(s))
# print(s.name)
# s.walk()
