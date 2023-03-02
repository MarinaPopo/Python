class Account:
    suffix = "RUB"

    def __init__(self, surname, num, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.value = value
        print(f"Счет №{self.__num}, принадлежащий {self.__surname}, был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.__num}, принадлежащий {self.__surname}, был закрыт.")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, s):
        self.__surname = s

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, n):
        self.__num = n

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, per):
        self.__percent = per

    def print_balance(self):
        print(f"Текущий баланс: {self.value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Проценты: {self.__percent:.0%}")
        print("-" * 20)


acc = Account(num='12345', surname='Долгих', percent=0.03, value=1000)
acc.print_info()
acc.surname = "Дюма"
acc.num = "54321"
acc.percent = 0.04
acc.print_info()


# class Account:
#     suffix = "RUB"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.value = value
#         print(f"Счет №{self.__num}, принадлежащий {self.__surname}, был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.__num}, принадлежащий {self.__surname}, был закрыт.")
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_surname(self, s):
#         self.__surname = s
#
#     def get_num(self):
#         return self.__num
#
#     def set_num(self, n):
#         self.__num = n
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_percent(self, per):
#         self.__percent = per
#
#     def print_balance(self):
#         print(f"Текущий баланс: {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print("-" * 20)


# acc = Account(num='12345', surname='Долгих', percent=0.03, value=1000)
# acc.print_info()
# acc.set_surname("Дюма")
# acc.set_num("54321")
# acc.set_percent(0.04)
# acc.print_info()
