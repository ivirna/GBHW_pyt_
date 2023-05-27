# Показать контакты
def show_contacts(phonebook_contacts):
    for contact in phonebook_contacts:
        if not contact["to_delete"]:
            print(contact["surname"] + " " + contact["name"] + " " + contact["patronymic"])
            print(contact["number"])
