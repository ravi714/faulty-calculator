# num1 =int(input("Enter You first Number: "))
# opraction = input("Enter Your Opraction: ")
# num2 = int(input("Enter You Secound Number: "))
# if (num1==45 and opraction=="*" and num2==3) or (num1==56 and opraction=="+" and num2==9) or (num1==56 and opraction=="/" and num2==6):
#     if num1==45 and opraction=="*" and num2==3:
#         print("555")
#     elif num1==56 and opraction=="+" and num2==9:
#         print("77")
#     elif num1==56 and opraction=="/" and num2==6:
#         print("4")
# else:
#     if opraction=="+":
#         print(int(num1+num2))
#     elif opraction=="-":
#         print(int(num1-num2))
#     elif opraction=="*":
#         print(int(num1*num2))
#     elif opraction=="/":
#         print(int(num1/num2))
#     else:
#         print("i don't Your Opraction")

#method 2
num1 =input("Enter You first Number: ")
opraction = input("Enter Your Opraction: ")
num2 = input("Enter You Secound Number: ")
strinmatch = (num1+opraction+num2)

wrongList = ["45*3","56+9","56/6"]
wronganslist = {"45*3":"555","56+9":"77","56/6":"4"}
if (num1+opraction+num2) in wrongList:
    print(wronganslist[strinmatch])
else:
    num1 = int(num1)
    num2 = int(num2)
    if opraction == "+":
        print(num1+num2)
    elif opraction=="-":
        print(num1-num2)
    elif opraction=="*":
        print(num1*num2)
    elif opraction=="/":
        print(num1/num2)
    else:
        print("i don't Your Opraction")
