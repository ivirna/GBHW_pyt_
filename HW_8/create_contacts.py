# Создание контакта
def create_contact(phonebook_contacts):
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

    print("Контакт создан")
    return True
