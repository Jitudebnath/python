class Student:
    college_name="ABC college"
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod 
    
    def welcome(self):
        print("welcome student")

    def get_marks(self):
        return self.marks  
        
s1 =Student("Jitu debnath",97)
s1.welcome()
print(s1.get_marks())       