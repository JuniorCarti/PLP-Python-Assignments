def add(x, y):
  """Adds two numbers."""
  return x + y


def subtract(x, y):
  """Subtracts two numbers."""
  return x - y


def multiply(x, y):
  """Multiplies two numbers."""
  return x * y


def divide(x, y):
  """Divides two numbers. Handles division by zero."""
  if y == 0:
    return "Cannot divide by zero!"
  return x / y


# Main calculator function
def calculator():
  """Provides a simple calculator interface."""

  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")

  while True:  # Keep running the calculator until the user chooses to exit
    try:
      choice = input("Enter choice(1/2/3/4): ")

      if choice not in ('1', '2', '3', '4'):
        print("Invalid input. Please enter 1, 2, 3, or 4.")
        continue  # Go back to the beginning of the loop

      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))

      if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

      elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

      elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

      elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

      break  # Exit the loop after performing the calculation

    except ValueError:
      print("Invalid input. Please enter numbers only.")
    except Exception as e:
      print(f"An error occurred: {e}")  # Handle other potential errors
    
    another_calculation = input("Do you want to do another calculation? (yes/no): ")
    if another_calculation.lower() != "yes":
        break
# Start the calculator
if __name__ == "__main__":
    calculator()