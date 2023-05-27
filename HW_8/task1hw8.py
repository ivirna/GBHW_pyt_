# Как использовать:
# python task1hw8.py [имя файла, по умолчанию phonebook.txt]

import sys

from show_contacts import show_contacts
from search_contacts import search_contacts_menu
from create_contacts import create_contact
from load_save_phonebook import load_phonebook, save_phonebook
from close_phonebook import close_phonebook


# Контакты в справочнике
phonebook_contacts = []
# Есть ли изменения
edited = False
# Путь к справочнику. По умолчанию phonebook.txt в текущей папке
phonebook_path = "phonebook.txt"


def main_menu():
    global edited

    print()
    print("1. Показать контакты")
    print("2. Найти/изменить/удалить контакт")
    print("3. Создать новый контакт")
    print("4. Сохранить справочник")
    print("0. Закрыть справочник")
    selected_option = input("Введите номер нужного пункта: ")
    print()

    if selected_option == "1":
        show_contacts(phonebook_contacts)
    elif selected_option == "2":
        if search_contacts_menu(phonebook_contacts):
            edited = True
    elif selected_option == "3":
        if create_contact(phonebook_contacts):
            edited = True
    elif selected_option == "4":
        if save_phonebook(phonebook_path, phonebook_contacts):
            edited = False
    elif selected_option == "0":
        close_phonebook(edited)
    else:
        print("Неизвестный пункт. Введите номер нужного пункта без лишних символов.")


# Задать путь к справочнику, если он указан
if len(sys.argv) > 1 and len(sys.argv[1]) > 0:
    phonebook_path = sys.argv[1]
print("Выбран справочник по адресу " + phonebook_path)

# Загрузить справочник и запускать меню, пока пользователь не выйдет из программы
phonebook_contacts = load_phonebook(phonebook_path)
while True:
    main_menu()
