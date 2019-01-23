#Tristan Meyer
#Third Point on Exponential Graph

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x3 = float(input("Enter x3: "))
sx3 = str(x3)
equation = y1*(y2/y1)**((x3-x1)/(x2-x1))
print("f("+sx3+") =",equation)