#Superclass and Subclass
class Employee:
    __minsalary = 20000  # Protected class variable
    __maxsalary = 200000  # Private class variable
    _companyName = "Tech Solutions"  # Public class variable
    def __init__(self, name, department, salary):
        #Private attributes
        self.__name = name
        self._department = department
        self.__salary = salary   
        
    #Private method
    def _showData(self):
        #การแสดงผลข้อมูล
        print(f"Name: {self.__name}, Position: {self._department}, Salary: {self.__salary}")

class Accounting(Employee):
    __department = "Accounting"  # Private class variable
    def __init__(self,name,salary):
        super().__init__(name,self.__department, salary)
        # super()._showData()  # Call the private method from the superclass

class IT(Employee):
    __department = "IT"  # Private class variable
    def __init__(self,name,salary):
        super().__init__(name,self.__department, salary)
        # super()._showData()  # Call the private method from the superclass

class HR(Employee):
    __department = "HR"  # Private class variable
    def __init__(self,name,salary):
        super().__init__(name,self.__department, salary)
        # super()._showData()  # Call the private method from the superclass

#การสร้างออบเจ็กต์
objAc = Accounting("Wanchana Saelue", 50000) 
objAc._showData()  # Call the private method from the subclass
objIt = IT("Naphat Saelue", 60000)       
objIt._showData()  # Call the private method from the subclass
objHr = HR("Nattapong Saelue", 70000)
objHr._showData()  # Call the private method from the subclass


#Print Public
# obj1._showData()
# obj2._showData()
# obj3._showData()

# Print class variables
# print(Accounting._Employee__minsalary)
# print(IT._companyName)
# print(HR._companyName)

