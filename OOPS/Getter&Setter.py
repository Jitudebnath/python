class Student:
    def __init__(self,name:str)->None:
        self.__name = name

    #Getter
    def get_name(self):
        return self.__name


    #Setter
    def set_name(self,new_name:str):
        self.__name = new_name   


s1 = Student("jitu")
print(s1.get_name())
#using setter for new name
s1.set_name("mohit")
print(s1.get_name())        