class Parent1:
    def getName(self):
        return "parent1"
class Parent2:
    def defName():
        return "Parent2"
class Parent3:
    def getName():
        return "Parent 3"

class Child(Parent1 , Parent2 , Parent3):
    def __init__(self):
        self.getAllParent()
    def getAllParent(self):
        print("trying to get all parents of this class")
        parent_list = []
        for base in Child.__bases__:
            parent_list.append(base)
        print(parent_list)
my_child = Child()
#parent_list = []
#print(my_child.__bases__)
#for base in Child.__bases__:
    #print(base,end=" ")

#print(my_child.getName())








