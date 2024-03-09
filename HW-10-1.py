from pulp import LpProblem, LpMaximize, LpVariable, LpStatus

# Створення моделі
model = LpProblem(name="Maximize_Products", sense=LpMaximize)

# Оголошення змінних рішення
lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# Об'єктивна функція (максимізація виробництва)
model += 3 * lemonade + 2 * fruit_juice, "Максимізація виробництва"

# Обмеження ресурсів
model += 2 * lemonade + fruit_juice <= 100, "Обмеження по воді"
model += 1 * lemonade <= 50, "Обмеження по цукру"
model += 1 * lemonade <= 30, "Обмеження по лимонному соку"
model += 2 * fruit_juice <= 40, "Обмеження по фруктовому пюре"

# Розв'язання моделі
model.solve()

# Виведення результатів
# print(f"Статус: {model.status}, {LpStatus[model.status]}")
print(f"Лимонад: {lemonade.varValue} одиниць")
print(f"Фруктовий сік: {fruit_juice.varValue} одиниць")
print(f"Загальне виробництво: {model.objective.value()} одиниць")
