class Soda:
    def __init__(self, add_t = None):
        if isinstance(add_t, str):
            self.add_t = add_t
        else:
            self.add_t = None
    def show_my_drink(self):
        if self.add_t != None:
            print(f'Газировка и {self.add_t}')
        else:
            print("Обычная газировка")
drink1 = Soda()
drink2 = Soda('малина')
drink3 = Soda(5)
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()