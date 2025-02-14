from functools import total_ordering
@total_ordering
class RealString:
    def __init__(self, some_str):
        self.some_str = str(some_str)

    def __eq__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.some_str) == len(other.some_str)

    def __lt__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.some_str) < len(other.some_str)
str1 = RealString('Молоко')
str2 = RealString('Абрикосы растут')
str3 = 'Золото'
str4 = [1, 2, 3]
print(str1 < str4)
print(str1 >= str2)
print(str1 == str3)