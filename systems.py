import json
#from opcode import name_op

from msg import *
from pathlib import Path
from prettytable import PrettyTable



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

if __name__ == "__main__":

    conf_path = Path().parent / 'settings.json'
    cont_path = Path().parent / 'contacts.json'

    contacts = l_json(cont_path)

    ctable = PrettyTable()

    ctable.field_names = ['#',
                          'ID',
                          'Name/Nickname',
                          'Surname',
                          'Phone',
                          'Comment',
                          'Tags',
                          'Created',
                          'Modified',
                          ]

    for i, (cid, info) in enumerate(contacts.items(), start=1):

        ctable.add_rows(
            [
                [i, cid,
                 info.get('name', 'N/A'),
                 info.get('surname', 'N/A'),
                 info.get('phone', 'N/A'),
                 info.get('comment', 'N/A'),
                 info.get('tags', 'N/A'),
                 info.get('created', 'N/A'),
                 info.get('modified', 'N/A')
                 ]
            ]
        )

    print(ctable)