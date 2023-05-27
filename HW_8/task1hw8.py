# Как использовать:
# python task1hw8.py [имя файла, по умолчанию phonebook.txt]

import sys
import os.path

# Контакты в справочнике
phonebook_contacts = []
# Есть ли изменения
edited = False
# Путь к справочнику. По умолчанию phonebook.txt в текущей папке
phonebook_path = "phonebook.txt"

# Открыть справочник
def open_phonebook():
    # Сбросить существующие контакты
    global phonebook_contacts
    phonebook_contacts = []

    # Если справочник найден, открыть его и прочитать контакты
    if os.path.isfile(phonebook_path):
        with open(phonebook_path, "r", encoding="utf8") as file:
            line_number = 0
            current_contact = {}
            for line in file.readlines():
                # На каждый контакт даётся пять строк
                contact_field_number = line_number % 5
                if contact_field_number == 0:
                    # Первая строка - фамилия
                    current_contact["surname"] = line.strip()
                elif contact_field_number == 1:
                    # Вторая строка - имя
                    current_contact["name"] = line.strip()
                elif contact_field_number == 2:
                    # Третья строка - отчество
                    current_contact["patronymic"] = line.strip()
                elif contact_field_number == 3:
                    # Четвёртая строка - номер телефона
                    current_contact["number"] = line.strip()
                elif contact_field_number == 4:
                    # Пятая строка - конец контакта
                    # id - внутренний номер контакта
                    current_contact["id"] = line_number // 5
                    # to_delete - метка удаления
                    current_contact["to_delete"] = False
                    phonebook_contacts.append(current_contact)
                    current_contact = {}
                line_number += 1
    else:
        print("Файл справочника будет создан при сохранении")


def show_contacts():
    for contact in phonebook_contacts:
        if not contact["to_delete"]:
            print(contact["surname"] + " " + contact["name"] + " " + contact["patronymic"])
            print(contact["number"])


# Редактирование контактов
def edit_contact(contact):
    global edited

    print()
    print("Редактируется контакт:")
    print(contact["surname"] + " " + contact["name"] + " " + contact["patronymic"])
    print(contact["number"])

    # Пометить контакт на удаление. Он удалится при записи, до записи он просто будет пропускаться
    delete_contact = input("Удалить контакт? [д/Н] ")
    if "д" in delete_contact.lower():
        phonebook_contacts[contact["id"]]["to_delete"] = True
        edited = True
        print("Контакт удалён")
        return

    new_surname = input("Введите новую фамилию или оставьте пустым, чтобы оставить старую: ")
    new_name = input("Введите новое имя или оставьте пустым, чтобы оставить старое: ")
    new_patronymic = input("Введите новое отчество или оставьте пустым, чтобы оставить старое: ")
    new_number = input("Введите новый номер телефона или оставьте пустым, чтобы оставить старый: ")

    if len(new_surname) > 0:
        phonebook_contacts[contact["id"]]["surname"] = new_surname
        edited = True
    if len(new_name) > 0:
        phonebook_contacts[contact["id"]]["name"] = new_name
        edited = True
    if len(new_patronymic) > 0:
        phonebook_contacts[contact["id"]]["patronymic"] = new_patronymic
        edited = True
    if len(new_number) > 0:
        phonebook_contacts[contact["id"]]["number"] = new_number
        edited = True

    if edited:
        print("Контакт изменён")
    else:
        print("Контакт оставлен без изменений")


# Меню редактирования контактов
def edit_contacts_menu(found_contacts):
    print()
    if len(found_contacts) > 0:
        print("Найдены контакты:")
        for i in range(len(found_contacts)):
            contact = found_contacts[i]
            # Вывод контакта в формате
            # 1. Фамилия Имя Отчество
            #    Номер
            # 2. Фамилия Имя Отчество
            #    Номер
            # ...
            # 10. Фамилия Имя Отчество
            #     Номер
            # ...
            print(str(i + 1) + ". " + contact["surname"] + " " + contact["name"] + " " + contact["patronymic"])
            print((" " * (len(str(i + 1)) + 2)) + contact["number"])

        selected_contact = input("Выберите контакт для редактирования или введите что-либо ещё для возврата: ")
        try:
            if 1 <= int(selected_contact) <= len(found_contacts):
                edit_contact(found_contacts[int(selected_contact) - 1])
        except ValueError:
            # Возврат, если ввод не переводится в число
            return
    else:
        print("Контактов по запросу не найдено")


def search_contacts_surname():
    search_term = input("Введите фамилию (целиком или частично, без учёта регистра): ").strip().lower()

    found_contacts = []
    for contact in phonebook_contacts:
        if search_term in contact["surname"].lower() and not contact["to_delete"]:
            found_contacts.append(contact)
    edit_contacts_menu(found_contacts)


def search_contacts_name():
    search_term = input("Введите имя (целиком или частично, без учёта регистра): ").strip().lower()

    found_contacts = []
    for contact in phonebook_contacts:
        if search_term in contact["name"].lower() and not contact["to_delete"]:
            found_contacts.append(contact)
    edit_contacts_menu(found_contacts)


def search_contacts_patronymic():
    search_term = input("Введите отчество (целиком или частично, без учёта регистра): ").strip().lower()

    found_contacts = []
    for contact in phonebook_contacts:
        if search_term in contact["patronymic"].lower() and not contact["to_delete"]:
            found_contacts.append(contact)
    edit_contacts_menu(found_contacts)


def search_contacts_number():
    search_term = input("Введите номер телефона (целиком или частично, без учёта символов): ").strip().lower()
    # Убрать все символы, кроме цифр
    search_term = "".join(filter(str.isdigit, search_term))

    found_contacts = []
    for contact in phonebook_contacts:
        if search_term in "".join(filter(str.isdigit, contact["number"].lower())) and not contact["to_delete"]:
            found_contacts.append(contact)
    edit_contacts_menu(found_contacts)


def search_contacts_menu():
    print("1. Поиск по фамилии")
    print("2. Поиск по имени")
    print("3. Поиск по отчеству")
    print("4. Поиск по номеру телефона")
    selected_option = input("Выберите нужный пункт или введите что-либо ещё для возврата: ")
    print()

    if selected_option == "1":
        search_contacts_surname()
    elif selected_option == "2":
        search_contacts_name()
    elif selected_option == "3":
        search_contacts_patronymic()
    elif selected_option == "4":
        search_contacts_number()
    else:
        return


# Создание контакта
def create_contact():
    global edited

    new_surname = input("Введите фамилию нового контакта: ")
    new_name = input("Введите имя нового контакта: ")
    new_patronymic = input("Введите отчество нового контакта: ")
    new_number = input("Введите номер телефона нового контакта: ")

    contact = {
        "surname": new_surname,
        "name": new_name,
        "patronymic": new_patronymic,
        "number": new_number,
        "id": len(phonebook_contacts),
        "to_delete": False
    }
    phonebook_contacts.append(contact)

    edited = True
    print("Контакт создан")


# Сохранение
def save_phonebook():
    global edited
    with open(phonebook_path, "w", encoding="utf8") as file:
        for contact in phonebook_contacts:
            if not contact["to_delete"]:
                file.write(contact["surname"] + "\n")
                file.write(contact["name"] + "\n")
                file.write(contact["patronymic"] + "\n")
                file.write(contact["number"] + "\n")
                file.write("\n")
        file.truncate()
        edited = False
        print("Справочник сохранён")

    # Перепрочитать справочник, чтобы убрать контакты, помеченные как удалённые
    open_phonebook()


def close_phonebook():
    if edited:
        print("Присутствуют несохранённые изменения!")
        selected_option = input("Действительно выйти? [д/Н] ")
        if "д" in selected_option.lower():
            sys.exit()
    else:
        sys.exit()


def main_menu():
    print()
    print("1. Показать контакты")
    print("2. Найти/изменить/удалить контакт")
    print("3. Создать новый контакт")
    print("4. Сохранить справочник")
    print("0. Закрыть справочник")
    selected_option = input("Введите номер нужного пункта: ")
    print()

    if selected_option == "1":
        show_contacts()
    elif selected_option == "2":
        search_contacts_menu()
    elif selected_option == "3":
        create_contact()
    elif selected_option == "4":
        save_phonebook()
    elif selected_option == "0":
        close_phonebook()
    else:
        print("Неизвестный пункт. Введите номер нужного пункта без лишних символов.")


# Задать путь к справочнику, если он указан
if len(sys.argv) > 1 and len(sys.argv[1]) > 0:
    phonebook_path = sys.argv[1]
print("Выбран справочник по адресу " + phonebook_path)

# Загрузить справочник и запускать меню, пока пользователь не выйдет из программы
open_phonebook()
while True:
    main_menu()
