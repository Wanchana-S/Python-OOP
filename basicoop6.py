#Encapsulation
# การสร้างคลาส
class Employee: 
    # #Public
    # #การสร้างเมธอด
    # def __init__(self, name, age, position, salary):
    #     #Public attributes
    #     self.name = name
    #     self.age = age
    #     self.position = position
    #     self.salary = salary   

    # #Public method
    # def showData(self):
    #     #การแสดงผลข้อมูล
    #     print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}")

    #========================================================================================================

    # #Protected
    # def __init__(self, name, age, position, salary):
    # #Protected attributes
    #     self._name = name
    #     self._age = age
    #     self._position = position
    #     self._salary = salary   

    # #Protected method
    # def _showData(self):
    #     #การแสดงผลข้อมูล
    #     print(f"Name: {self._name}, Age: {self._age}, Position: {self._position}, Salary: {self._salary}")

    #========================================================================================================

    #Private
    def __init__(self, name, age, position, salary):
    #Private attributes
        self._name = name
        self._age = age
        self.__position = position
        self.__salary = salary   
        self._showData()

    #Private method
    def _showData(self):
        #การแสดงผลข้อมูล
        print(f"Name: {self._name}, Age: {self._age}, Position: {self.__position}, Salary: {self.__salary}")

    #========================================================================================================
    
#การสร้างออบเจ็กต์
obj1 = Employee("Wanchana Saelue", 29, "Software Engineer", 50000)

#Print Public
# obj1._salary = 50000 # Changing the salary
# obj1._showData()  
#========================================================================================================

#Print Protected
# obj1._name = "Naphat Saelue"  # Changing the name
# obj1._showData()

#========================================================================================================

#Print Private      
obj1.__salary = 60000 # Not changing the salary, as it's private
obj1._name = "Naphat Saelue"  # Changing the name
obj1._showData() 

