# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    for i in range(n):
        if i == 0 or i == n - 1:
            result += "*" * n + "\n"
        else:
            result += "*" + " " * (n - 2) + "*\n"
    
    return result.rstrip()

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
    result = ""
    for i in range(1, n+1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1) 
        result += spaces + stars + "\n" 
    return result.rstrip()