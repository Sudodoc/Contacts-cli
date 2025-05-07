from pathlib import Path
from initialize import fist_run_ini
from systems import l_json, s_json
from contacts import list_, options_menu, search_
from msg import *
from contclass import ContactList

msg = msg_eng
conf_path = Path().parent / 'settings.json'
cont_path = Path().parent / 'contacts.json'

if not conf_path.exists():                  # Проверка первого запуска программы.
                                            # Случай, если файл settings.json отсутствует.

    settings, msg, contacts = fist_run_ini()
    s_json(conf_path, settings)
    s_json(cont_path, contacts)


settings = l_json(conf_path)                # Вариант, когда файл settings.json существует.

if settings["fist_run_ini"]:

    settings, msg, contacts = fist_run_ini()
    s_json(conf_path, settings)
    s_json(cont_path, contacts)

elif settings["language"] == 'ru': msg = msg_ru         # Устанавливаем язык интерфейса на русский, если он задан в settings

else:
    if settings["language"] != 'en':
        print(msg_eng['SYS']['CONF_ERR'])
        exit()


count = settings['counter']                 # Загружаем счетчик
# contacts = l_json(cont_path)                # Загружаем контакты и count после всех инициализаций наконец-то

contacts = ContactList(l_json(cont_path), settings, msg)

print(msg['INI']['HELLO_'])

while True:

    options_menu(msg)                       # собсна главное меню
    option = input(msg['OPT']['SELECT'])


    if option == '1':


        contacts.all()
        contacts.mod(cont_path)


    elif option == '2':

        count += 1
        new_contact, go_back = contacts.new(count)

        if go_back:
            count -= 1
            continue

        else:

            if contacts.vault is None:
                contacts.vault = {}

            contacts.vault.update(new_contact)
            s_json(cont_path, contacts.vault)
            settings['counter'] = count
            s_json(conf_path, settings)


    elif option == '3':                         # Global search

        print(msg['OPT']['SEARCH_MENU'])

        while True:

            s_string = (input('\nSearch: ')).lower()

            if   s_string == 'x' : break
            elif s_string == 'h!': print(msg['OPT']['SEARCH_HELP'])
            elif s_string == '' or s_string == ' ' : print(msg['SYS']['IN_ERR'])

            else:

                found_contacts = search_(contacts.vault, s_string)

                if not found_contacts: print(msg['SYS']['NOT_FOUND'])

                elif len(found_contacts) == 1:
                    one_id = list(found_contacts.keys())[0]
                    contacts.mod(cont_path, one_id)

                else:
                    list_(found_contacts)
                    contacts.mod(cont_path)


    elif option == 'x':
        print(msg['OPT']['BYE'])
        exit()

    else:
        print(msg['SYS']['IN_ERR'])


