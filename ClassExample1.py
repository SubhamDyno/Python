from tkinter import *
import datetime

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class A:
    def __init__(self, name, surname):
        self.name = name;
        self.surname = surname;
        print(f"{name}, {self.surname}");
    def show(self,n):
        self.n = n;
        print(self.n);

obj = A(name = "SUbham", surname="Patra");
obj.show(n="P");

class B(A):
    pass
obj2 = B("Hello","HI");

