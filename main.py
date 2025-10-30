import sys
import math

def get_coefficient_from_user(index, prompt):
    while True:
        try:
            coefficient_str = sys.argv[index]
            coefficient = float(coefficient_str)
            if index == 1 and coefficient == 0.0:
                print('Коэффициент A не может быть равен нулю :( ')
                continue
            return coefficient
        except IndexError:
            print(prompt)
            coefficient_str = input()
            try:
                coefficient = float(coefficient_str)
                if index == 1 and coefficient == 0.0:
                    print('Коэффициент A не может быть равен нулю :( ')
                    continue
                return coefficient
            except ValueError:
                print('Неправильный формат числа. Повторите ввод')
        except ValueError:
            print('Неверный формат ввода. Повторите ввод')

def get_roots(a, b, c):
    roots_t = []
    D = b*b - 4*a*c

    if D < 0:
        pass
    elif D == 0:
        t = -b/(2*a)
        roots_t.append(t)
    else:
        sqrtD = math.sqrt(D)
        t1 = (-b + sqrtD)/(2*a)
        t2 = (-b - sqrtD)/(2*a)
        roots_t.append(t1)
        roots_t.append(t2)

    roots_x = set()
    for t in roots_t:
        if t > 0:
            root1 = math.sqrt(t)
            root2 = -math.sqrt(t)
            roots_x.add(root1)
            roots_x.add(root2)
        elif t == 0:
            roots_x.add(0.0)

    return sorted(roots_x)

def main():
    a = get_coefficient_from_user(1, 'Введите коэффициент A: ')
    b = get_coefficient_from_user(2, 'Введите коэффициент B: ')
    c = get_coefficient_from_user(3, 'Введите коэффициент C: ')

    roots = get_roots(a, b, c)
    len_roots = len(roots)

    if len_roots == 0:
        print('Нет действительных корней')
    elif len_roots == 1:
        print('Один действительный корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два действительных корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три действительных корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре действительных корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))

if __name__ == "__main__":
    main()
