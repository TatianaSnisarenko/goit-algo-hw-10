import pulp

if __name__ == "__main__":

    # Ініціалізація моделі
    model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

    # Визначення змінних
    # Кількість продукту Лемонад
    x = pulp.LpVariable('Lemonade', lowBound=0, cat='Continious')
    # Кількість продукту Фруктовий сік
    y = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continious')

    # Функція цілі (Максимізація виробництва продуктів
    model += x + y, "Profit"

    # Додавання обмежень
    model += 2*x + y <= 100  # Обмеження на кількість води
    model += x <= 50  # Обмеження на кількість цукру
    model += x <= 30  # Обмеження на лимонний сік
    model += 2*y <= 40  # Обмеження на фруктовий сік

    # Розв'язання моделі
    model.solve()

    # Вивід результатів
    print("Виробляти Лемонаду:", x.varValue)
    print("Виробляти Фруктового соку:", y.varValue)
