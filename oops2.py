class School:
    name = "Pritam"
    def getAge(self):
        return "20"
class SubSchool(School):
    def _init_(self):
        print("Child Constructor")
    def getParentName(self):
        return "Pritam"
    def getName(self):
        return "Gayathri"
my_school = SubSchool()
print(my_school.getParentName())
print(my_school.getName())
print(my_school.getAge())
    