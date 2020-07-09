# The input function returns whatever the user entered into the commandline before pressing enter
# The value is returned as string
num1 = input("Insert the first number. ")
num2 = input("Insert the second number. ")

# We assume a perfect user.
# int() tries to transform a string into an integer number value
# This transformation is called "casting" or a "cast".
# It will give an error and abort the script if the transformation does not succeed
num1 = int(num1)
num2 = int(num2)

# create a new variable and assign it the result of the addition of the two numbers
result = num1 + num2
# cast the result, which is a number, into a string to print it back to the commandline and thus to the user
print("result: " + str(result))
