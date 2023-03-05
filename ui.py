import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите название заметки: '), number)
    body = check_len_text_input(
        input('Введите описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nЭто программа 'Заметки'. Имеются следующие функции:\n\n1 - Вывод всех заметок из файла\n2 - Добавление заметки\n3 - Удаление заметки\n4 - Редактирование заметки\n5 - Выборка заметок по дате\n6 - Просмотр заметки по id\n7 - Выход\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Работа приложения завершена.")