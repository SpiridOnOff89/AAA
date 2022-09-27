DATA = 'Corp_Summary.csv'


def make_report(file_name: str) -> dict:
    """
    Создает отчет из файла csv и сохраяет
    его в переменной report типа dict
    """

    import csv

    report = {}

    with open(file_name, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=",")

        counter = 0
        for row in reader:
            if counter == 0:
                counter += 1
                continue

            info = row[0].split(';')
            department = info[1]
            team = info[2]
            salary = int(info[5])

            if department not in report:
                report[department] = {
                    'teams': set(),
                    'salaries': [],
                    'quantity': 0
                }
            report[department]['teams'].add(team)
            report[department]['salaries'].append(salary)
            report[department]['quantity'] += 1

        for department in report:
            report[department]['mean_salary'] = round(sum(report[department]['salaries']) /
                                                      len(report[department]['salaries']))
            report[department]['min_salary'] = min(report[department]['salaries'])
            report[department]['max_salary'] = max(report[department].pop('salaries'))

    return report


def print_table(data: list, title: str) -> None:
    """Печатает таблицу из двумерного массива"""
    max_columns = []
    for col in zip(*data):
        len_el = []
        for el in col:
            len_el.append(len(el))
        max_columns.append(max(len_el))

    for i in range(len(data)):
        line = '-' * (sum(max_columns) + 5 * len(data[0]) + 1)
        if i == 0:
            print(line)
            print('|' + ' ' * ((len(line) - len(title)) // 2 - 1) + title.upper() +
                  ' ' * (len(line) - len(title) - ((len(line) - len(title)) // 2) - 1) +
                  '|')
            print(line)
        print('|', end='')
        for j in range(len(max_columns)):
            print(' ', data[i][j], ' ' * (max_columns[j] - len(data[i][j])), end=' |')
        print('')
        if i == 0:
            print(line)
        if i == len(data) - 1:
            print(line)


def print_teams(report: dict) -> None:
    """Создает двумерный массив структуры департаментов
    и печатает его функцией print_table"""
    data = [[department for department in report]]

    # считаю максимально встречающееся количество команд в департаменте
    # для последующего определения размера двумерного массива,
    # заодно перевожу множество teams в массив для последующей обработки в цикле по индексу
    max_teams = 0
    for department in report:
        report[department]['teams'] = list(report[department]['teams'])
        if len(report[department]['teams']) > max_teams:
            max_teams = len(report[department]['teams'])

    # добавляю в массив data списки с названиями команд - будущие строки таблицы
    for i in range(max_teams):
        line = []
        for j in range(len(report)):
            if len(report[data[0][j]]['teams']) >= i + 1:
                line.append(report[data[0][j]]['teams'][i])
            else:
                line.append('')
        data.append(line)

    print_table(data, 'структура департаментов')


def print_report(report: dict) -> None:
    """"Создает двумерный массив со сведениями сводного отчета и
    печатает его функцией print_table"""
    data = [['Департамент', 'Чел.', 'Средняя зарплата', 'Зарплатная вилка']]
    for department in report:
        data.append(
            [
                department,
                str(report[department]['quantity']),
                str(report[department]['mean_salary']),
                f"{report[department]['min_salary']} - {report[department]['max_salary']}"
            ]
        )
    print_table(data, 'сводный отчет')


def save_report(report: dict) -> None:
    """Сохраняет сводный отчет по департаментам в файл"""
    import csv
    file_name = input('Введите название файла: ') + '.csv'
    with open(file_name, mode='w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Департамент', 'Численность', 'Вилка зарплат', 'Средняя зарплата'])
        for department in report:
            writer.writerow(
                [
                    department,
                    report[department]['quantity'],
                    f'{report[department]["min_salary"]} - {report[department]["max_salary"]}',
                    report[department]['mean_salary']
                ]
            )
    print(f'Отчет записан в файл "{file_name}".')


def menu(data: str) -> None:
    """Предлагает пользователю выбрать один
    из трех вариантов действий и
    запускает соответствующую функцию"""
    commands = ['1', '2', '3', '0']
    actions = [print_teams, print_report, save_report]

    report = make_report(data)

    while True:
        command = input("""Выберите вариант действия:
1. Вывести структуру департаментов
2. Вывести сводный отчет
3. Сохранить сводный отчет в файл
0. Выйти\n""")

        while command not in commands:
            command = input(f'Введите команду: {" / ".join(commands)}\n')

        if command == '0':
            return

        func = actions[int(command) - 1]
        func(report)

        answers = ['y', 'n']
        answer = input(f"Желаете продолжиить?\nВыберите {'/'.join(answers)}\n")

        while answer not in ['y', 'n']:
            answer = input(f"Выберите: {' / '.join(answers)}\n")

        if answer == 'n':
            return


if __name__ == '__main__':
    menu(DATA)
