#Inheritance
class Employee:
    __minsalary = 20000  # Protected class variable
    __maxsalary = 200000  # Private class variable
    _companyName = "Tech Solutions"  # Public class variable
    def __init__(self, name, position, salary):
        #Private attributes
        self.__name = name
        self._position = position
        self.__salary = salary   
        
    #Private method
    def _showData(self):
        #การแสดงผลข้อมูล
        print(f"Name: {self.__name}, Position: {self.__position}, Salary: {self.__salary}")

class Accounting(Employee):
    __department = "Accounting"  # Private class variable
    def __init__(self):
        pass

class IT(Employee):
    __department = "IT"  # Private class variable
    def __init__(self):
        pass

class HR(Employee):
    __department = "HR"  # Private class variable
    def __init__(self):
        pass

#การสร้างออบเจ็กต์
objAc = Accounting("Wanchana Saelue","Acc", 50000) 
objIt = IT("Naphat Saelue","Senior Software Engineer", 60000)       
objHr = HR("Nattapong Saelue","HR Manager", 70000)

#Print Public
# obj1._showData()
# obj2._showData()
# obj3._showData()

# Print class variables
print(Accounting._Employee__minsalary)
# print(IT._companyName)
# print(HR._companyName)

