# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    return ""

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    for i in range (1,n+1):
        for j in range (1, i+1):
            result += str(j) 
        result += "\n"
    return(result.strip())


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    numbers = [] 
    for i in range (1,n+1):
        numbers.append(i)
    result = sum(numbers)

    return result

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    return ""
