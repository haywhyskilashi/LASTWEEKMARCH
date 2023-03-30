# Write a Python program to test whether a
# passed letter is a vowel or not

userInputed = str(input("Enter a character"))
if (userInputed == 'a' or userInputed == 'e' or userInputed == 'i' or userInputed == '0' or userInputed == 'u'):
    print("This is a vowel")
else:
    print("This is a consonant")


name = input("Enter your name please")

def hello():
    print("Hello" + name)
    print("Youre welcome here")

hello()


# return statement = functions send python values/object
# back to the caller. These values/objects are known as
# the functions return values


def multiply(number1, number2):
    result = number1 * number2
    return result

print(multiply(6, 8))


# nested functions call = function calls inside other function
# calls innermost function calls are resolved first returned
# value is used as argument for the next outer functions

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))


# scope = the region that a variable is recognized. A variable
# is only available from inside the region it is created.
# A global and locally scoped versions of a variable can be created



# 65. Write a Python program that converts
# seconds into days, hours, minutes, and seconds.

seconds = input("Enter the seconds")
minutes = input("Enter the minutes")
hours = input("Enter the hour")
days = input("Enter the days")

time = seconds + minutes + hours + days
print(time)




