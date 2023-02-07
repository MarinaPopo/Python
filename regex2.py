import re

tel = """
+7 499 456-45-78
+74994564578
7 (499) 456 45 78
7 (499) 456-45-78"""

reg = r"\+?7\s?(?:\(\d{3}\)|\d{3})\s?\d{3}[-\s]?\d{2}[-\s]?\d{2}"
print(re.findall(reg, tel))


# Сколько в списке отрицательных чисел
neg = 0


def neg_count(lst):
    global neg
    if len(lst) == 0:
        return neg
    elif lst[0] < 0:
        neg += 1
    return neg_count(lst[1:])


print(neg_count([-2, 3, 8, -11, -4, 6]))
