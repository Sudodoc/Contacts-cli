import json
from msg import *

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