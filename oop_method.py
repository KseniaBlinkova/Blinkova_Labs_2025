import math
import sys

class Biquadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if self.a == 0:
            return "Не биквадратное (a=0)"
        d = self.b ** 2 - 4 * self.a * self.c
        if d < 0:
            return "Нет корней"
        y1 = (-self.b + math.sqrt(d)) / (2 * self.a)
        y2 = (-self.b - math.sqrt(d)) / (2 * self.a)
        roots = []
        for y in (y1, y2):
            if y >= 0:
                x = math.sqrt(y)
                roots.append(x)
                roots.append(-x)
        if not roots:
            return "Корней нет"
        return "Корни: " + ", ".join(map(str, sorted(roots)))

def read_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Нужно ввести число!")

def main():
    if len(sys.argv) == 4:
        try:
            a, b, c = map(float, sys.argv[1:4])
        except ValueError:
            print("Аргументы должны быть числами. Перехожу к интерактивному вводу.")
            a = b = c = None
    else:
        a = b = c = None
    if a is None:
        print("Решаем биквадратное уравнение ax⁴ + bx² + c = 0")
        a = read_float("a = ")
        b = read_float("b = ")
        c = read_float("c = ")
    my_biquad = Biquadratic(a, b, c)
    print(my_biquad.solve())


if __name__ == "__main__":
    main()
