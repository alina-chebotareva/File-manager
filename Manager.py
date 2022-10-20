from functions import*
import os
def main():
    instructions = input('Введите путь к файлу с инструкциями')
    with open(instructions) as file:
        work_folder=file.read()
    os.chdir(work_folder)
    while True:
        command = int(input('Выберите команду: \n'
                        '1.	Создание папки (с указанием имени) \n'
                        '2.	Удаление папки по имени \n'
                        '3.	Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх \n'
                        '4.	Создание пустых файлов с указанием имени  \n'
                        '5.	Запись текста в файл \n'
                        '6.	Просмотр содержимого текстового файла \n'
                        '7.	Удаление файлов по имени \n'
                        '8.	Копирование файлов из одной папки в другую \n'
                        '9.	Перемещение файлов \n'
                        '10. Переименование файлов\n'
                        '11. Выход из файлового менеджера\n'
                            ))
        if command == 1:
            name = input('Введите название папки')
            create_new_folder(name)
        elif command == 2:
            name = input('Введите название папки')
            delete_folder(name)
        elif command == 3:
            choice=int(input('Выберите: \n'
                         '1. Зайти в папку по имени \n'
                         '2. Выйти на уровень вверх \n'))
            if choice==1:
                name = input('Введите название папки')
                open_folder(name)
            elif choice==2:
                previuos_dir(work_folder)
        elif command == 4:
            name = input('Введите название файла')
            create_file(name)
        elif command == 5:
            name = input('Введите название файла')
            text = input('Введите текст')
            text_input(name, text)
        elif command == 6:
            name = input('Введите название файла')
            read_file(name)
        elif command == 7:
            name = input('Введите название файла')
            delete_file(name)
        elif command == 8:
            name = input('Введите название файла')
            new_dir = input('Введите путь к новой папке ')
            copy_file(name, new_dir)
        elif command == 9:
            name = input('Введите название файла: ')
            new_dir = input('Введите путь к новой папке')
            move_file(name, new_dir)
        elif command == 10:
            name = input('Введите название файла')
            new_name = input('Введите новое название файла')
            rename_file(name, new_name)
        elif command == 11:
            exit()
        else:
            print('Неверный запрос. Выберите команду 1-12')
if __name__ == '__main__':
    main()



