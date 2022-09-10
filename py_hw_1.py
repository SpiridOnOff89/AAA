def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар.'
        'Взять ей зонтик? ☂ '
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Зонтик утке не к лицу - в баре треснет подлецу.\n'
          'Пожалеет ли утка об этом?')
    answers = {'да': 'Видимо подлец хорош. Селезень садится в Porshe.',
               'нет': 'Хорошо, что утка пьёт! И не вспомнит про тот зонт.'}
    answer = ''
    while answer not in answers:
        answer = input(f'Выберите: {"/".join(list(answers.keys()))}\n')
    print(answers[answer])


def step2_no_umbrella():
    print('Правильно! Зачем ей зонт? После бара лучше понт!\n'
          'Домой утка пойдет под дождём?')
    answers = {'да': 'Дождь промоет перья ей - будет чище всех зверей!',
               'нет': 'Утка умная у нас - экстрасенсом будет "класс!".'}
    answer = ''
    while answer not in answers:
        answer = input(f'Выберите: {"/".join(list(answers.keys()))}\n')
    print(answers[answer])


if __name__ == '__main__':
    step1()
