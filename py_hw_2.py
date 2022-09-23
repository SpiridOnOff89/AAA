DATA = 'Corp_Summary.csv'


def make_report(file_name: str) -> dict:
    """Создает отчет из файла csv и сохраяет его в переменной report типа dict"""

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


def print_teams(report: dict) -> None:
    """Печатает список команд каждого департамента"""
    for department in report:
        print(f'Команды департамента "{department}":')
        n = 1
        for team in report[department]['teams']:
            print(f'{n}) {team}')
            n += 1
        print()


def print_stats(report: dict) -> None:
    """Печатает численность, вилку зарплат и среднюю зарплату по департаментам"""
    for department in report:
        print(f'Департамент "{department}"')
        print(f'Численность: {report[department]["quantity"]}')
        print(f'Вилка зарплат: {report[department]["min_salary"]} - {report[department]["max_salary"]}')
        print(f'Средняя зарплата: {report[department]["mean_salary"]}')
        print()


def print_table(report:dict) -> None:

    data = []
    for department in report:
        data.append(
            [
            department,
            str(report[department]['quantity']),
            str(report[department]['mean_salary']),
            f"{report[department]['min_salary']} - {report[department]['max_salary']}"
            ]
        )

    max_columns = []
    for col in zip(*data):
        len_el = []
        for el in col:
            len_el.append(len(el))
        max_columns.append(max(len_el))





def save_stats(report: dict) -> None:
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
    """Предлагает пользователю выбрать один из трех вариантов действий"""
    commands = ['1', '2', '3']
    actions = [print_teams, print_table, save_stats]

    report = make_report(data)

    command = input(
        """Выберите вариант действия:
1. Вывести команды департаментов
2. Вывести сводный отчет
3. Сохранить сводный отчет в файл
"""
    )

    while command not in commands:
        command = input(f'Введите команду: {" / ".join(commands)}\n')

    func = actions[int(command) - 1]
    func(report)



if __name__ == '__main__':
    menu(DATA)
