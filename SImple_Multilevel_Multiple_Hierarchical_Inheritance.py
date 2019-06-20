class A:
    
    def __init__(self, dog, name):
        self.name = name;
        self.dog = dog;
    def show(self):
        print(self.name, self.dog)
    
        

objA = A("DOG", "NAME");


class B(A):
    def __init__(self, fname, dname):
        self.fname = fname;
        self.dname = dname;
    def show(self):
        print(self.fname, self.dname)
     
    print("Simple Inheritance A-> B")
    objA.show()
    

objB = B("Mahima", "Kumari")


class C(B):
    print("Multilevel Inheritance A-> B -> C")
    objB.show();
    objA.show();

class D(A):
    print("Hierarchical Inheritance Base class : A , Derived class :B, D, A->B&D -")
    objA.show()

class F:
    
    def __init__(self, cat, name):
        self.name = name;
        self.cat = cat;
    def show(self):
        print(self.name, self.cat)
class E(A, F):
    objA.show()
    objF = F("CAT", "NAME");
    print("Multiple Inheritance A,F -> E: ")
    objF.show()
    
    
    


    

