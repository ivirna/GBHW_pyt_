import sys


# Закрыть справочник
def close_phonebook(edited):
    if edited:
        print("Присутствуют несохранённые изменения!")
        selected_option = input("Действительно выйти? [д/Н] ")
        if "д" in selected_option.lower():
            sys.exit()
    else:
        sys.exit()
