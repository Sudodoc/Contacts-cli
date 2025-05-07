import json
from msg import *
from datetime import datetime


def s_json(f_path, content):
    with f_path.open('w', encoding='UTF-8') as file:
        json.dump(content, file, indent=4, ensure_ascii=False)


def l_json(f_path):
    with f_path.open('r', encoding='UTF-8') as file:
        return json.load(file)


def set_lang(lg='en'):
    if lg == 'en':
        print(msg_eng['INI']['EN_OK'])
        return 'en'

    elif lg == 'ru':
        print(msg_ru['INI']['RU_OK'])
        return 'ru', msg_ru

    else:
        print(msg_eng['SYS']['LANG_ERR'])
        return None


def get_formated_datetime():
    timenow = datetime.now()
    return timenow.strftime("%d.%m.%y|%H:%M:%S")


if __name__ == "__main__":


    from pathlib import Path
    from contclass import ContactList

    conf_path = Path().parent / 'settings.json'
    cont_path = Path().parent / 'contacts.json'

    # from contacts import list_, SimpleProfile
    # contacts = l_json(cont_path)
    # list_(contacts)

    contacts = ContactList(l_json(cont_path), l_json(conf_path), msg_eng)
    print(contacts)
    contacts.all()



