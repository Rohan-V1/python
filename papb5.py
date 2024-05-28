import sqlite3
import sys

con = sqlite3.connect('std.db')
print("Opened database successfully")
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS student
 (regno INT PRIMARY KEY NOT NULL,
 name TEXT NOT NULL,
 mark1 REAL,
 mark2 REAL,
 mark3 REAL);''')
print("Table student created successfully")


def student_exists(rno):
    data = (rno,)
    sql = "SELECT * FROM student WHERE regno=?"
    r = c.execute(sql, data).fetchall()
    if len(r) > 0:
        return True
    else:
        return False


def add_student():
    regno = input("Enter the register number: ")
    if student_exists(regno):
        print("Student already exists. Try again.")
    else:
        name = input("Enter student name: ")
        mark1 = float(input("Enter mark in subject 1: "))
        mark2 = float(input("Enter mark in subject 2: "))
        mark3 = float(input("Enter mark in subject 3: "))
        data = (regno, name, mark1, mark2, mark3)
        sql = "INSERT INTO student VALUES(?,?,?,?,?)"
        c.execute(sql, data)
        con.commit()
        print("Student added successfully")


def display_student():
    sql = "SELECT * FROM student"
    r = c.execute(sql).fetchall()
    if len(r) == 0:
        print("There are no records")
    for i in r:
        print("-" * 50)
        print("Student register number:", i[0])
        print("Student name:", i[1])
        print("Mark in subject 1:", i[2])
        print("Mark in subject 2:", i[3])
        print("Mark in subject 3:", i[4])
        print("-" * 50)


def remove_student():
    regno = input("Enter the register number of the student to be removed: ")
    if student_exists(regno):
        sql = "DELETE FROM student WHERE regno=?"
        data = (regno,)
        c.execute(sql, data)
        con.commit()
        print("Student removed.")
    else:
        print("Student does not exist. Try again.")


def menu():
    print('''
    1. Add student.
    2. Display all student details.
    3. Remove student.
    4. Exit''')
    ch = int(input("Enter your choice: "))
    if ch == 1:
        add_student()
    elif ch == 2:
        display_student()
    elif ch == 3:
        remove_student()
    elif ch == 4:
        c.execute("DROP TABLE IF EXISTS student")
        sys.exit()
    else:
        print("Please enter a correct choice")
    menu()


menu()
