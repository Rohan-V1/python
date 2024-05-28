import sqlite3
import sys

con = sqlite3.connect('Emp.db')
print("Opened database successfully")
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employee
             (empno INT PRIMARY KEY,
              name TEXT NOT NULL,
              salary REAL);''')
print("Table employee created successfully")


def employee_exists(eno):
    data = (eno,)
    sql = "SELECT * FROM employee WHERE empno=?"
    r = c.execute(sql, data).fetchall()
    if len(r) > 0:
        return True
    else:
        return False


def add_employee():
    empno = input("Enter employee number: ")
    if employee_exists(empno):
        print("Employee already exists. Try again.")
    else:
        name = input("Enter employee name: ")
        salary = float(input("Enter employee salary: "))
        data = (empno, name, salary)
        sql = "INSERT INTO employee VALUES(?,?,?)"
        c.execute(sql, data)
        con.commit()
        print("Employee added successfully")


def display_using_empno():
    empno = input("Enter the employee number whose details to be displayed: ")
    print("-" * 40)
    if employee_exists(empno):
        data = (empno,)
        sql = "SELECT * FROM employee WHERE empno=?"
        r = c.execute(sql, data).fetchall()
        for i in r:
            print("Employee number:", i[0])
            print("Employee name:", i[1])
            print("Employee salary:", i[2])
            print("-" * 40)
    else:
        print("Employee does not exist")


def display_using_salary():
    min_salary = input("Enter the minimum salary: ")
    max_salary = input("Enter the maximum salary: ")
    sql = "SELECT * FROM employee WHERE salary BETWEEN ? AND ?"
    data = (min_salary, max_salary)
    r = c.execute(sql, data).fetchall()
    if len(r) == 0:
        print("There is no employee whose salary is between", min_salary, "and", max_salary)
    else:
        print("Employee details whose salary is between", min_salary, "and", max_salary)
        print("-" * 40)
        for i in r:
            print("Employee number:", i[0])
            print("Employee name:", i[1])
            print("Employee salary:", i[2])
            print("-" * 40)


def menu():
    print('''
    1. Add new employee.
    2. Display employee using employee no.
    3. Display employee using salary range.
    4. Exit.''')
    ch = int(input("Enter your choice: "))
    if ch == 1:
        add_employee()
    elif ch == 2:
        display_using_empno()
    elif ch == 3:
        display_using_salary()
    elif ch == 4:
        c.execute("DROP TABLE IF EXISTS employee")
        sys.exit()
    else:
        print("Please enter the correct choice")
    menu()


menu()
