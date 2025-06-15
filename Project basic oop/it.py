from employee import Employee

class IT(Employee):
    __department = "IT"  # Private class variable
    __skill = ["Python", "Java", "C++"]  # Example skill set
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,self.__department, salary)
        self.__experience = experience
        self.__skill = skill    

    def _showData(self):
        #การแสดงผลข้อมูล
        super()._showData()
        print(f"Experience: {self.__experience} years, Skills: {', '.join(self.__skill)}")
        print("==================================")

    def __str__(self):
        # Override the __str__ method to provide a string representation of the object
        return f"IT(Name: {self._Employee__name}, Department: {self._department}, Salary: {self._Employee__salary}, Experience: {self.__experience} years, Skills: {', '.join(self.__skill)})"