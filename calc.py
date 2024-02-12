def calculate(num1, num2, operator):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    return num1 / num2
  else:
    print("Invalid operator")
    return None

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = calculate(num1, num2, operator)
print(f"{num1} {operator} {num2} = { result : }")
