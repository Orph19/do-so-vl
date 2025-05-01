#!/usr/bin/env python3
class Parent:
    def __init__(self, prop1):
        self.prop1 = prop1

    def method1(self):
        return "Parent method1" 

class Child(Parent):
    def __init__(self,prop1,prop2):
        super().__init__(prop1)
        self.prop2 = prop2

    def adit1(self):
        return "Child adit1"       
    
dude = Child("person","alive")

print(dude.method1())
print(dude.adit1())
