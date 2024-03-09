def rect():
    l=int(input("enter the length: "))
    b=int(input("Enter the breadth: "))
    a=l*b
    print("Area of rectangle= ",a)
def sqr():
    s=int(input("enter the side: ")) 
    a=s*s
    print("area of square= ",a)
def cir():
    pi=3.14
    r=int(input("Enter the radius: ")) 
    a=pi*r*r
    print("The area of circle is= ",a)
def tri():
    h=int(input("Enter height: "))
    b=int(input("Enter breadth: "))
    a=0.5*h*b
    print("Area of triangle: ",a)

print("------SQUARE------")  
sqr()
print("------CIRCLE------")
cir()
print("-----RECTANGLE-----")
rect()
print("-----TRIANGLE-----")
tri()


