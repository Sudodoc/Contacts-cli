from typing import Dict
from prettytable import PrettyTable
from systems import get_formated_datetime, s_json
from random_id import gen_id
from contacts import show_one_

class ContactList:

    def __init__(self, contacts: Dict[str, dict], settings: dict, msg: dict):
        self.vault = contacts
        self.conf = settings
        self.m = msg


    def __str__(self):

        show_dict = ''
        for cid, info in self.vault.items():
            show_dict += f'{cid} : {info}\n'
        return show_dict


    def all(self):

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

        for i, (cid, info) in enumerate(self.vault.items(), start=1):
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

        print('', ctable, sep='\n')


    def new(self, xcount=1, return_id=False, cancel=False):

        c_tele = input(self.m['ASK']['TELE'])
        if c_tele == 'x':
            contact = {}
            cancel = True
            return contact, cancel
        elif c_tele == '':
            c_tele = 'N/A'

        c_name = input(self.m['ASK']['NAME'])
        if c_name == 'x':
            contact = {}
            cancel = True
            return contact, cancel
        elif c_name == '':
            c_name = 'N/A'

        c_surn = input(self.m['ASK']['SURN'])
        if c_surn == 'x':
            contact = {}
            cancel = True
            return contact, cancel
        elif c_surn == '':
            c_surn = 'N/A'

        c_note = input(self.m['ASK']['NOTE'])
        if c_note == 'x':
            contact = {}
            cancel = True
            return contact, cancel
        elif c_note == '':
            c_note = 'N/A'

        c_tags = list(set((input(self.m['ASK']['TAGS'])).lower().split(' ')))
        if c_tags[0] == 'x':
            contact = {}
            cancel = True
            return contact, cancel
        elif c_tags[0] == '':
            c_tags = 'N/A'

        c_time = get_formated_datetime()
        c_id = gen_id(c_name, c_surn, c_tele, xcount)

        if c_name != 'N/A':
            c_name = c_name.capitalize()
        if c_surn != 'N/A':
            c_surn = c_surn.capitalize()

        contact = {c_id:    {
                            'N': xcount,
                            'name': c_name,
                            'surname': c_surn,
                            'phone': c_tele,
                            'comment': c_note,
                            'tags': c_tags,
                            'created': c_time,
                            'modified': None,
                            }
        }

        if not return_id:
            return contact, cancel
        else:
            return contact, cancel, c_id

    def mod(self, mcont_path, one_id=''):

        while True:

            if not one_id:
                detect_id = (input(self.m['OPT']['DETECT_ID'])).upper()  # Задаем ID контакта, который будем редактировать
            else:
                detect_id = one_id  # Случай если найдена только одна запись

            if detect_id == 'X':
                break

            elif detect_id in self.vault:  # Проверяем, есть ли введенный ID в списке контактов

                show_one_(self.vault, detect_id)
                del_or_mod = input(self.m['ASK']['DEL_OR_MOD']).lower()  # Уточняем, будем редактировать или удалять.

                if del_or_mod == 'x':
                    break

                elif del_or_mod == 'm':  # Редактируем

                    while True:

                        ask_key = (input(self.m['ASK']['KEY'])).lower()  # Спрашиваем, что именно будем редактировать

                        if ask_key == 'x':
                            break

                        elif ask_key == 'tags':  # Отдельно прописываем обработку тегов
                            new_tags = list(set((input(self.m['ASK']['TAGS'])).lower().split(' ')))

                            if new_tags == 'x': break

                            self.vault[detect_id][ask_key] = new_tags
                            self.vault[detect_id]['modified'] = get_formated_datetime()  # Фиксируем время изменения
                            s_json(mcont_path, self.vault)

                        elif ask_key in self.vault[detect_id] and ask_key != 'tags':
                            new_item = input(self.m['ASK']['ITEM'])

                            if new_item == 'x': break

                            self.vault[detect_id][ask_key] = new_item
                            self.vault[detect_id]['modified'] = get_formated_datetime()
                            s_json(mcont_path, self.vault)

                            print(self.m['SYS']['MODIFY_OK'].format(detect_id=detect_id))

                        else:
                            print(self.m['SYS']['FIELD_ERR'])

                elif del_or_mod == 'd':  # Удалить контакт

                    while True:

                        del_confirm = input(self.m['ASK']['CONFIRM_DEL']).lower()

                        if del_confirm == 'y':

                            del self.vault[detect_id]
                            s_json(mcont_path, self.vault)
                            print(self.m['SYS']['DEL_OK'].format(detect_id=detect_id))
                            break

                        elif del_confirm == 'n':
                            break

                        else:
                            print(self.m['SYS']['IN_ERR'])

                else:
                    print(self.m['SYS']['IN_ERR'])

            else:
                print(self.m['SYS']['ID_ERR'])