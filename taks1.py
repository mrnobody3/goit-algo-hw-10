# task1_production_optimization.py
import pulp

# Створення задачі (максимізація)
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні — кількість продуктів
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = pulp.LpVariable("FruitJuice", lowBound=0, cat="Integer")

# Обмеження ресурсів
water_limit = 100
sugar_limit = 50
lemon_juice_limit = 30
fruit_puree_limit = 40

# Додавання обмежень
model += 2 * lemonade + 1 * fruit_juice <= water_limit        # Вода
model += 1 * lemonade <= sugar_limit                          # Цукор
model += 1 * lemonade <= lemon_juice_limit                    # Лимонний сік
model += 2 * fruit_juice <= fruit_puree_limit                 # Фруктове пюре

# Цільова функція — максимізація кількості продуктів
model += lemonade + fruit_juice

# Розв'язання задачі
model.solve()

print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Лимонад: {lemonade.value()}")
print(f"Фруктовий сік: {fruit_juice.value()}")
print(f"Максимальна кількість продуктів: {pulp.value(model.objective)}")
