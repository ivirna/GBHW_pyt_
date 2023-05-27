# Редактирование контактов
def edit_contact(contact, phonebook_contacts):
    edited = False

    print()
    print("Редактируется контакт:")
    print(contact["surname"] + " " + contact["name"] + " " + contact["patronymic"])
    print(contact["number"])

    # Пометить контакт на удаление. Он удалится при записи, до записи он просто будет пропускаться
    delete_contact = input("Удалить контакт? [д/Н] ")
    if "д" in delete_contact.lower():
        phonebook_contacts[contact["id"]]["to_delete"] = True
        print("Контакт удалён")
        return True

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
    return edited


# Меню редактирования контактов
def edit_contacts_menu(found_contacts, phonebook_contacts):
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
                return edit_contact(found_contacts[int(selected_contact) - 1], phonebook_contacts)
        except ValueError:
            # Возврат, если ввод не переводится в число
            return False
    else:
        print("Контактов по запросу не найдено")
        return False
