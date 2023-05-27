from edit_contacts import edit_contacts_menu


def search_contacts_surname(phonebook_contacts):
    search_term = input("Введите фамилию (целиком или частично, без учёта регистра): ").strip().lower()

    found_contacts = []
    for contact in phonebook_contacts:
        if search_term in contact["surname"].lower() and not contact["to_delete"]:
            found_contacts.append(contact)
    return edit_contacts_menu(found_contacts, phonebook_contacts)


def search_contacts_name(phonebook_contacts):
    search_term = input("Введите имя (целиком или частично, без учёта регистра): ").strip().lower()

    found_contacts = []
    for contact in phonebook_contacts:
        if search_term in contact["name"].lower() and not contact["to_delete"]:
            found_contacts.append(contact)
    return edit_contacts_menu(found_contacts, phonebook_contacts)


def search_contacts_patronymic(phonebook_contacts):
    search_term = input("Введите отчество (целиком или частично, без учёта регистра): ").strip().lower()

    found_contacts = []
    for contact in phonebook_contacts:
        if search_term in contact["patronymic"].lower() and not contact["to_delete"]:
            found_contacts.append(contact)
    return edit_contacts_menu(found_contacts, phonebook_contacts)


def search_contacts_number(phonebook_contacts):
    search_term = input("Введите номер телефона (целиком или частично, без учёта символов): ").strip().lower()
    # Убрать все символы, кроме цифр
    search_term = "".join(filter(str.isdigit, search_term))

    found_contacts = []
    for contact in phonebook_contacts:
        if search_term in "".join(filter(str.isdigit, contact["number"].lower())) and not contact["to_delete"]:
            found_contacts.append(contact)
    return edit_contacts_menu(found_contacts, phonebook_contacts)


def search_contacts_menu(phonebook_contacts):
    print("1. Поиск по фамилии")
    print("2. Поиск по имени")
    print("3. Поиск по отчеству")
    print("4. Поиск по номеру телефона")
    selected_option = input("Выберите нужный пункт или введите что-либо ещё для возврата: ")
    print()

    if selected_option == "1":
        return search_contacts_surname(phonebook_contacts)
    elif selected_option == "2":
        return search_contacts_name(phonebook_contacts)
    elif selected_option == "3":
        return search_contacts_patronymic(phonebook_contacts)
    elif selected_option == "4":
        return search_contacts_number(phonebook_contacts)
    else:
        return False
