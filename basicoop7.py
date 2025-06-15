#Encapsulation
# การสร้างคลาส
class Employee: 
    def __init__(self, name, age, position, salary):
    #Private attributes
        self.__name = name
        self.__age = age
        self.__position = position
        self.__salary = salary   
        # self._showData()

    #Private method
    def _showData(self):
        #การแสดงผลข้อมูล
        print(f"Name: {self.getName()}, Age: {self.getAge()}, Position: {self.getPosition()}, Salary: {self.getSalary()}")

    #Setter method
    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age
    
    def setPosition(self, position):
        self.__position = position

    def setSalary(self, salary):
        self.__salary = salary
    
    #Getter method
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    def getPosition(self):
        return self.__position
    
    def getSalary(self):
        return self.__salary

    
#การสร้างออบเจ็กต์
obj1 = Employee("Wanchana Saelue", 29, "Software Engineer", 50000)
obj1.setName("Naphat Saelue") 
obj1.setAge(30)
obj1.setPosition("Senior Software Engineer")
obj1.setSalary(60000)

#Print Public
obj1._showData() 

