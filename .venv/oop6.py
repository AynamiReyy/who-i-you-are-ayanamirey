class Recipe:
    def __init__(self, meal = None, ingredients = None):
        self.meal = meal
        self.ingredients = ingredients
    def print_ingredients(self):
        print(f'Ингредиенты для {self.meal}')
        for i in self.ingredients:
            print(i)
    def cook(self):
        print(f'Сегодня мы готовим {self.meal}')
        print(f'Выполняем инструкцию по приготовлению блюда {self.meal}')
        print(f'Блюдо {self.meal}')
spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])

spaghetti.print_ingredients()

spaghetti.cook()

cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])

cake.print_ingredients()