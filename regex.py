import re

# Пароль может содержать цифры, лат. буквы, дефис, собака, подчеркивание, длина 6-18

pw = 'my-p@ssw0rd'
reg1 = r"^[\dA-z@_-]{6,18}$"
print(re.findall(reg1, pw))

# Найти дату в формате dd/mm/YYYY

s = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зарегистрированы максимумы осадков"
reg2 = r"(?:0[1-9]|[12][0-9]|3[01])/(?:0?[1-9]|1[0-2])/(?:[12]\d{3})"
print(re.findall(reg2, s))
