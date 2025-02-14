class TriangleChecker:
    def __init__(self, a = None, b = None, c = None):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if isinstance(self.a, int) and isinstance(self.b, int) and isinstance(self.c, int):
            if self.a + self.b > self.c and self.c + self.b > self.a and self.a + self.c > self.b:
                print("Ура, можно построить треугольник!")
            elif self.a < 0 or self.b < 0 or self.c < 0:
                print("С отрицательными числами ничего не выйдет!")
            else:
                print("Жаль, но из этого треугольник не сделать.")
        else:
            print("Нужно вводить только числа!")
triangle1 = TriangleChecker(2, 3, 4)
triangle1.is_triangle()
triangle2 = TriangleChecker(77, 3, 4)
triangle2.is_triangle()
triangle3 = TriangleChecker(77, 3, 'Сторона3')
triangle3.is_triangle()
triangle4 = TriangleChecker(77, -3, 4)
triangle4.is_triangle()