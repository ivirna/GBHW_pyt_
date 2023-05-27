import os.path


# Открыть справочник
def load_phonebook(phonebook_path):
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

    return phonebook_contacts


# Сохранение
def save_phonebook(phonebook_path, phonebook_contacts):
    with open(phonebook_path, "w", encoding="utf8") as file:
        for contact in phonebook_contacts:
            if not contact["to_delete"]:
                file.write(contact["surname"] + "\n")
                file.write(contact["name"] + "\n")
                file.write(contact["patronymic"] + "\n")
                file.write(contact["number"] + "\n")
                file.write("\n")
        file.truncate()
        print("Справочник сохранён")

    # Перепрочитать справочник, чтобы убрать контакты, помеченные как удалённые
    load_phonebook(phonebook_path)
    return True
