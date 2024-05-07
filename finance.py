import time

class ManagerFinance:
    def __init__(self) -> None:
        self.expenses: list = []
        self.income: list = []
        self.show_balance()

    def show_balance(self):
        ''''Просмотр баланса '''
        self.expenses: list = []
        self.income: list = []
        count: int = 0
        expenses_int: int = 0
        income_int: int = 0
        with open('financedoc.txt', 'r', encoding='utf-8') as file:
            data = []
            for line in file:
                count += 1
                data.append(line.replace('\n', ''))
                if count == 4:
                    if data[1].split(':')[1].replace(' ','') == 'Расход':
                        self.expenses.append(data)
                        expenses_int += int(data[2].split(':')[1])
                    elif data[1].split(':')[1].replace(' ','') == 'Доход':
                        self.income.append(data)
                        income_int += int(data[2].split(':')[1])
                    data = []
                    count = 0
        return income_int - expenses_int

    def add_file(self, data: str, category, summ, descr):
        '''Добавление новой записи о расходе или доходе'''
        data = data.split()[0]
        with open('financedoc.txt', 'a', encoding='utf-8') as file:
            if isinstance(summ, int):
                file.write(f'\nДата: {data}\n')
                file.write(f'Категория: {category}\n')
                file.write(f'Сумма: {summ}\n')
                file.write(f'Описание: {descr}')
                print("Успешно")
            else:
                print('Сумма должна быть числом')

    def update_file(self, date, new_sum):
        '''Обновление суммы в файле для конкретной даты'''
        with open('financedoc.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        for i in range(len(lines)):
            if lines[i].startswith(f'Дата: {date}'):
                lines[i+2] = f'Сумма: {new_sum}\n'
                print("Успешно")
                break
        else:
            print(f'Запись с датой {date} не найдена')
            return

        with open('financedoc.txt', 'w', encoding='utf-8') as file:
            file.writelines(lines)

    def show_date(self, date):
        '''Поиск по дате'''
        self.show_balance()
        main = self.expenses + self.income
        new = []
        for i in main:
            if i[0].split(': ')[1] == date:
                print(i[0])
                print(i[1])
                print(i[2])
                print(i[3])
                new.append(i)
        return new
    
    def show_expenses(self):
        '''Просмотр расходов'''
        self.show_balance()
        return self.expenses

    def show_income(self):
        '''Просмотр доходов'''
        self.show_balance()
        return self.income


fin = ManagerFinance()


while True:
    print("-------------------------------------------------------------")
    print("Meню")
    print("1 Вывод баланса")
    print("2 Добавление записи")
    print("3 Обновление суммы в файле для конкретной даты")
    print("4 Поиск по дате")
    print("5 Просмотр расходов")
    print("6 Просмотр доходов")
    print("7 Выход")
    print("-------------------------------------------------------------")
    print()
    try:
        choise = int(input("Выберите пункт меню: "))

        if choise == 1:
            print("Ваш баланс составляет: ", fin.show_balance())
            time.sleep(1)
        if choise == 2:
            # data: str, category, summ, descr
            try:
                data = input("Введите дату (в таком формате 2024-05-04): ")
                category = input("Введите категорию(Доход/Расход): ")
                summ = int(input("Введите сумму: "))
                descr = input("Введите описание: ")
                fin.add_file(data, category, summ, descr)
                time.sleep(1)
            except ValueError as e:
                print("Введен не правильный тип данных")
                time.sleep(1)
        if choise == 3:
            try:
                data = input("Введите дату (в таком формате 2024-05-04): ")
                summ = int(input("Введите сумму: "))
                fin.update_file(data, summ)
                time.sleep(1)
            except ValueError as e:
                print("Введен не правильный тип данных")
                time.sleep(1)
        if choise == 4:
            data = input("Введите дату (в таком формате 2024-05-04): ")
            fin.show_date(data)
            time.sleep(1)
        if choise == 5:
            print()
            for inc in fin.show_expenses():
                for i in inc:
                    print(i)
                print()
            time.sleep(1)
        if choise == 6:
            print()
            for inc in fin.show_income():
                for i in inc:
                    print(i)
                print()
            time.sleep(1)
        if choise == 7:
            break

    except ValueError:
        print("Введен не правильный тип данных")


    
