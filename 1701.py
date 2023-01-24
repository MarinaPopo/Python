# Функция считает сумму, декоратор - среднее арифметическое

def avg(fn):
    def wrap(*f_args):
        average = round(fn(*f_args) / len(f_args), 2)
        print("Среднее арифметическое чисел", str(f_args)[1: -1], "=", average)

    return wrap


@avg
def add(*args):
    print("Сумма чисел", str(args)[1: -1], "=", sum(args))
    return sum(args)


add(2, 3, 3, 4)
