# Function to print a diamond pattern
def print_diamond(size):
    # Upper part (pyramid)
    for row in range(1, size+1):
        print(" " * (size - row), end="")
        print(" ".join(str(num) for num in range(1, row+1)))
    
    # Lower part (inverted pyramid)
    for row in range(size-1, 0, -1):
        print(" " * (size - row), end="")
        print(" ".join(str(num) for num in range(1, row+1)))

# Function to print an equilateral triangle pattern
def print_equilateral_triangle(size):
    for row in range(1, size+1):
        print(" " * (size - row), end="")
        print(" ".join(str(num) for num in range(1, row+1)))

# Function to print a pyramid pattern
def print_pyramid(size):
    for row in range(1, size+1):
        print(" " * (size - row), end="")
        print(" ".join(str(num) for num in range(1, row+1)))

# Function to print a square pattern
def print_square(size):
    for row in range(size):
        print(" ".join(str(num+1) for num in range(size)))

# Function to print a left-aligned triangle pattern
def print_left_triangle(size):
    for row in range(1, size+1):
        print(" ".join(str(num) for num in range(1, row+1)))

# Function to display a menu and let the user choose a pattern
def choose_pattern():
    while True:  # This loop will keep asking the user until they decide to exit
        print("\nSelect a pattern to generate:")
        print("1. Pyramid")
        print("2. Square")
        print("3. Left-Aligned Triangle")
        print("4. Equilateral Triangle")
        print("5. Diamond")
        print("6. Exit")
        
        # Get user's choice
        choice = int(input("Enter your choice (1-6): "))
        
        if choice == 6:
            print("Exiting the program. Goodbye!")
            break  # Exit the loop and the program
        
        # Ask for size input if not exiting
        size = int(input("Enter the size of the pattern: "))
        
        # Generate the selected pattern
        if choice == 1:
            print_pyramid(size)
        elif choice == 2:
            print_square(size)
        elif choice == 3:
            print_left_triangle(size)
        elif choice == 4:
            print_equilateral_triangle(size)
        elif choice == 5:
            print_diamond(size)
        else:
            print("Invalid choice! Please select a valid option.")

# Start the program by showing the pattern menu
choose_pattern()
