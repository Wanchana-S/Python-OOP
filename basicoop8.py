#Class Variable and Instance Variable
# การสร้างคลาส
class Employee: 
    #Class Variable
    _minSalary = 30000  # Protected class variable
    __maxSalary = 200000  # Private class variable  
    _companyName = "Tech Solutions"  # Public class variable

    def __init__(self, name, age, position, salary):
    #instance attributes
        self.__name = name
        self._age = age
        self._position = position
        self.__salary = salary   
        # self._showData()

    #Private method
    def _showData(self):
        #การแสดงผลข้อมูล
        print(f"Name: {self.__name}, Age: {self._age}, Position: {self._position}, Salary: {self.__salary}")



    
#การสร้างออบเจ็กต์
obj1 = Employee("Wanchana Saelue", 29, "Software Engineer", 50000)

#Print Public
print(Employee._companyName)
# obj1._showData() 

