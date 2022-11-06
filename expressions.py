
# Defines function on how to perform the operations
def calc_math_expression(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == ':':
        if num2 != 0:
            return num1 / num2
    else:
        return None

# Defines function which turns an input into numbers ready to perform the operation
def calc_math_expression_from_str(str_input):
    parameters = str_input.split()
    return calc_math_expression(float(parameters[0]), float(parameters[2]), parameters[1])

#str_input = input("Please input first number, the operator, and the second number: ")
#print(calc_math_expression_from_str(str_input))

# Defines function which gives the largest and smallest numbers out of a list of three
def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    numbers = [num1, num2, num3]
    numbers.sort()
    return (numbers[-1], numbers[0])

#print(find_largest_and_smallest_numbers(num1=3, num2=5, num3=4))

# Imports the sqrt skill and specifies the math module
from math import sqrt
# Defines function which provides quadratic solution as a tuple (solution1, solution2)
def quadratic_equation_solver(a, b, c):
    if a == 0:
        return (None, None)
    else:
        root = (b*b) - (4*a*c)
        if root < 0:
            return (None, None)
        elif root == 0:
            x = (-b) / (2*a)
            return (x, None)
        elif root > 0:
            x1 = ((-b) + sqrt(root)) / (2*a)
            x2 = ((-b) - sqrt(root)) / (2*a)
            return (x1, x2)

#print(quadratic_equation_solver(a=1, b=1.5, c=-1))

# Defines function to turn input into a, b, c numbers ready for the quadratic solution finder
def quadratic_equation_solver_from_user_input(quad_input):
    quad_numbers = quad_input.split()
    quad_numbers[0] = float(quad_numbers[0])
    quad_numbers[1] = float(quad_numbers[1])
    quad_numbers[2] = float(quad_numbers[2])
    if quad_numbers[0] == 0:
        print("'a' cannot be zero") #should this be return?
    elif len(quad_numbers) != 3:
        print("Please only input three numbers") #should this be return?
    else:
        return quadratic_equation_solver(quad_numbers[0], quad_numbers[1], quad_numbers[2])

#quad_input = input("Please input the three numbers for a b, c, seperated by spaces:")
#print(quadratic_equation_solver_from_user_input(quad_input))

# Defines temperature checker function
def temp_checker(min_temp, temp_1, temp_2, temp_3):
    if temp_1 > min_temp and temp_2 > min_temp:
        return True
    elif temp_1 > min_temp and temp_3 > min_temp:
        return True
    elif temp_2 > min_temp and temp_3 > min_temp:
        return True
    else:
        return False