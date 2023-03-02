# Функція додавання
def add(x, y):
    return x + y

# Функція віднімання
def subtract(x, y):
    return x - y

# Функція множення
def multiply(x, y):
    return x * y

# Функція ділення
def divide(x, y):
    return x / y

# Вивід меню
print("Виберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

# Введення операції
choice = input("Введіть номер операції (1/2/3/4): ")

# Введення чисел
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

# Обчислення результату
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))

else:
    print("Вибрано неправильну операцію")
