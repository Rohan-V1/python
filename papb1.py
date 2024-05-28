class Employee:
    def __init__(self):
        self.empno = 0
        self.name = ""
        self.dept = ""
        self.designation = ""
        self.age = 0
        self.salary = 0

    def getdetails(self):
        self.empno = int(input("Enter employee number: "))
        self.name = input("Enter employee name: ")
        self.dept = input("Enter department name: ")
        self.designation = input("Enter designation: ")
        self.age = int(input("Enter age: "))
        self.salary = int(input("Enter salary: "))

    def showdata(self):
        print("\nEmployee number:", self.empno)
        print("Name:", self.name)
        print("Department:", self.dept)
        print("Designation:", self.designation)
        print("Age:", self.age)
        print("Salary:", self.salary)

    @staticmethod
    def search(eno, L):
        for emp in L:
            if eno == emp.empno:
                return emp
        return None

def main():
    n = int(input("Enter total number of employees: "))
    L = []
    for i in range(n):
        emp = Employee()
        emp.getdetails()
        L.append(emp)
    print("\nPrinting details of all the employees...")
    for emp in L:
        emp.showdata()
    eno = int(input("Enter the employee number you want to search: "))
    e = Employee.search(eno, L)
    if e is not None:
        e.showdata()
    else:
        print("Employee does not exist")

if __name__ == "__main__":
    main()
