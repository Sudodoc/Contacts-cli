from pathlib import Path
from initialize import fist_run_ini
from systems import *
from contacts import create_contact, list_, options_menu, modify_or_delete, search_
from msg import *

msg = msg_eng
conf_path = Path().parent / 'settings.json'
cont_path = Path().parent / 'contacts.json'

# check-------------------
# print(conf_path, conf_path.exists(), cont_path, conf_path.exists(), sep='|')
# -----------------------

if not conf_path.exists():                  # Проверка первого запуска программы.
                                            # Случай, если файл settings.json отсутствует.

    settings, msg, contacts, count = fist_run_ini()

    # check---------
    # print(settings, contacts, sep='\n')
    # --------------

    s_json(conf_path, settings)
    s_json(cont_path, contacts)


settings = l_json(conf_path)                # Вариант, когда файл settings.json существует.

if settings["fist_run_ini"]:

    settings, msg, contacts, count = fist_run_ini()
    s_json(conf_path, settings)
    s_json(cont_path, contacts)

elif settings["language"] == 'ru':          # Устанавливаем язык интерфейса на русский, если он задан в settings
    msg = msg_ru

else:
    if settings["language"] != 'en':
        print(msg_eng['SYS']['CONF_ERR'])
        exit()


count = settings['counter']                 # Загружаем счетчик
contacts = l_json(cont_path)                # Загружаем контакты и count после всех инициализаций наконец-то"""

# check--------------------------------------------------------
# print(settings, contacts, msg['INI']['LANG_CHECK'], sep='\n')
# -------------------------------------------------------------


print(msg['INI']['HELLO_'])
while True:

    options_menu(msg)                       # собсна главное меню
    option = input(msg['OPT']['SELECT'])


    if option == '1':

        list_(contacts)
        modify_or_delete(msg, contacts, cont_path)


    elif option == '2':

        count += 1
        new_contact, go_back = create_contact(msg, count)

        if go_back:
            count -= 1
            continue

        else:

            if contacts is None:
                contacts = {}

            contacts.update(new_contact)
            # check---------------------------
            #for key, item in contacts.items():
            #    print(f'{key} : {item}')
            # --------------------------------
            s_json(cont_path, contacts)

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

                found_contacts = search_(s_string, contacts)

                if not found_contacts:
                    print(msg['SYS']['NOT_FOUND'])

                else:
                    list_(found_contacts)
                    modify_or_delete(msg, contacts, cont_path)


    elif option == 'x':
        print(msg['OPT']['BYE'])
        exit()

    else:
        print(msg['SYS']['IN_ERR'])


