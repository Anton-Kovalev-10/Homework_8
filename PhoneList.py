def read_file(data_path):
    with open(data_path, 'r', encoding = 'UTF-8') as file:
        return file.readlines()

def wright_file(data_path, data, key):
    with open(data_path, key, encoding = 'UTF-8') as file:
        file.write(f'\n{data}')

def parsing_data(data, name):
    my_string = ''
    for line in data:
        if name in line.lower() and len(line) > 3:
            my_string += line
    return my_string

def chenge_delete(data, name, action):
    check = True
    data_file = read_file(data_path)
    for index, line in enumerate(data_file)
        if name in line.lower() and len(line) > 3:
            data_file[index] = action
            with open(data_path, 'w', encoding = 'UTF = 8') as file:
                for line in data_file:
                    file.write(f'{line}')
            check = False
    if check:
        print(f'Name "{name}" not found')


data_path = 'Seminar/data'
result_path = 'Seminar/result'

to_do = int(input('Change action: '
                  '\n1 - show info'
                  '\n2 - export info in result file'
                  '\n3 - import new record'
                  '\n4 - change info in file'
                  '\n5 - delete info in line\n: '))

if to_do != 3:
    name = input('Input First or Last name: ').lower()

if to_do == 1:
    data_file = read_file(data_path)
    print(parsing_data(data_file, name))

if to_do == 2:
    data_file = read_file(data_path)
    result_data = parsing_data((data_file, name))
    wright_file(result_path, result_data, 'w')

if to_do == 3:
    data_file = input('Введите ФИО и номер')
    wright_file((data_file, 'a'))

if to_do == 4:
    action = input('Измените запись: ')
    chenge_delete(data_path, name, action)


if to_do == 5:
    action = ''
    chenge_delete(data_path, name, action)