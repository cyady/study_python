# #Example1
#
# print("this is starting point of program...")
# print("this is starting point of program...")
# print("this is starting point of program...")
# try:
#     print(x)
# except:
#     print("Exception occured")
# print("this is end of the program..")
# print("this is end of the program..")
# print("this is end of the program..")

# #Example2
# print("this is starting point of program...")
# print("Program in progress")
# try:
#     print(10/5) #(10/5)2.0    #(10/0)ZeroDivisionError: division by zero
# except ZeroDivisionError:
#     print("Exception occured..handled..")
# print("program completed..")

# #Example3 : Multiple except blocks  - try, except else, finally
#
# try:
#     num1, num2 = 10, 0
#     result = num1/num2
#     print("result is: ", result)
# except ZeroDivisionError:
#     print("Thrown ZeroDivisionError exception...")
# except SyntaxError:
#     print("Thrown Syntax error exception...")
# except:
#     print("exception handled..")
# else:
#     print("No exceptions occured...")
# finally:
#     print("always execute..")

#Example4 : raising our own exceptions
def enterage(num):
    if num<0:
        raise ValueError("Only Integers are allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")
print("checking number is even or odd by calling function..")
num=-1
try:
    enterage(num)
except ValueError:
    print("Value Error exception occured and handled..")
print("program completed..")





















