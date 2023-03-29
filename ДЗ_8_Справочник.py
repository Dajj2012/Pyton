import module1
def choose_action(phonebook):
    while True:
        print('Что вы хотите сделать?')
        user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Добавить контакт\n\
4 - Изменить контакт\n5 - Удалить контакт\n6 - Просмотреть все контакты\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            file_to_add = input('Введите название импортируемого файла: ')
            module1.import_data(file_to_add, phonebook)
        elif user_choice == '2':
            contact_list = module1.read_file_to_dict(phonebook)
            module1.find_number(contact_list)
        elif user_choice == '3':
            module1.add_phone_number(phonebook)
        elif user_choice == '4':
            module1.change_phone_number(phonebook)
        elif user_choice == '5':
            module1.delete_contact(phonebook)
        elif user_choice == '6':
            module1.show_phonebook(phonebook)
        elif user_choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue

if __name__ == '__main__':
    file = 'Phonebook.txt'
    choose_action(file)