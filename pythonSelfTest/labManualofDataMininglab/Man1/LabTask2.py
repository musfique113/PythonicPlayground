# Write a Python program that accepts an integer (n) and computes the value of n + nn + nnn.

# Explanation:

# First, we ask the user to input an integer n using the input function and store it in a variable of the same name.

# Next, we create two new variables nn and nnn which will store the values of n + nn and n + nn + nnn respectively. We use the str function to convert n into a string, and then concatenate two or three copies of it using the + operator to create the desired values, which we then convert back into integers using the int function.

# Finally, we add up the values of n, nn, and nnn and store the result in a variable called result.

# Finally, we use the print function to display the result

n = int(input("Enter n: "))
nn = int(str(n)+str(n))
nnn = int(str(n)+str(n)+str(n))
print("n:",n)
print("nn:",nn)
print("nnn:",nnn)
print("Sum of n+nn+nnn:",n+nn+nnn)