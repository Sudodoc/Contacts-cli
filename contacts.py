from random_id import gen_id
from msg import msg_eng
from datetime import datetime
from systems import s_json


def get_formated_datetime():
    timenow = datetime.now()
    f_timenow = timenow.strftime("%d.%m.%y|%H:%M:%S")
    return f_timenow


def create_contact(cmsg, xcount=1, return_id=False, cancel=False):

    c_tele = input(cmsg['ASK']['TELE'])
    if c_tele == 'x':
        contact = {}
        cancel =True
        return contact, cancel
    elif c_tele == '':
        c_tele = 'N/A'

    c_name = input(cmsg['ASK']['NAME'])
    if c_name == 'x':
        contact = {}
        cancel =True
        return contact, cancel
    elif c_name == '':
        c_name = 'N/A'

    c_surn = input(cmsg['ASK']['SURN'])
    if c_surn == 'x':
        contact = {}
        cancel =True
        return contact, cancel
    elif c_surn == '':
        c_surn = 'N/A'

    c_note = input(cmsg['ASK']['NOTE'])
    if c_note == 'x':
        contact = {}
        cancel =True
        return contact, cancel
    elif c_note == '':
        c_note = 'N/A'

    c_tags = list(set((input(cmsg['ASK']['TAGS'])).lower().split(' ')))
    if c_tags[0] == 'x':
        contact = {}
        cancel =True
        return contact, cancel
    elif c_tags[0] == '':
        c_tags = 'N/A'

    c_time = get_formated_datetime()
    c_id   = gen_id(c_name, c_surn, c_tele, xcount)

    if c_name != 'N/A':
        c_name = c_name.capitalize()
    if c_surn != 'N/A':
        c_surn = c_surn.capitalize()

    contact = {c_id:    {
                        'N'         : xcount,
                        'name'      : c_name,
                        'surname'   : c_surn,
                        'phone'     : c_tele,
                        'comment'   : c_note,
                        'tags'      : c_tags,
                        'created'   : c_time,
                        'modified'  : None,
                        }
    }

    if not return_id:
        return contact, cancel
    else:
        return contact, cancel, c_id


def list_(lcontacts):

    for i, (c_id, info) in enumerate(lcontacts.items(), start=1):

        print(f'\n#{i}.ID: {c_id}, {info.get('created', 'N/A')}')
        print(f'Name/Nickname : {info.get('name', 'N/A')}')
        print(f'Surname       : {info.get('surname', 'N/A')}')
        print(f'Phone number  : {info.get('phone', 'N/A')}')
        print(f'Comment   : {info.get('comment')}')
        print(f'Tags : {info.get('tags', 'N/A')}')



def show_one_(scontacts,detect_id):

    print(f'\nID: {detect_id}, {scontacts[detect_id].get('created', 'N/A')}')
    print(f'Name/Nickname : {scontacts[detect_id].get('name', 'N/A')}')
    print(f'Surname       : {scontacts[detect_id].get('surname', 'N/A')}')
    print(f'Phone number  : {scontacts[detect_id].get('phone', 'N/A')}')
    print(f'Comment   : {scontacts[detect_id].get('comment')}')
    print(f'Tags : {scontacts[detect_id].get('tags', 'N/A')}')
    print('---')


def options_menu(omsg):

    print(omsg['OPT']['TITLE_'])
    print(omsg['OPT']['LIST_A'])
    print(omsg['OPT']['ADDNEW'])
    print(omsg['OPT']['SEARCH'])
    print(omsg['OPT']['X'])


def modify_or_delete(mmsg, mcontacts, mcont_path, one_id=False ):

    while True:

        if not one_id: detect_id = (input(mmsg['OPT']['DETECT_ID'])).upper()    # Задаем ID контакта, который будем редактировать
        else:          detect_id = one_id                                       # Случай если найдена только одна запись

        if detect_id == 'X':
            break

        elif detect_id in mcontacts:                                # Проверяем, есть ли введенный ID в списке контактов
            show_one_(mcontacts, detect_id)

            del_or_mod = input(mmsg['ASK']['DEL_OR_MOD']).lower()  # Уточняем, будем редактировать или удалять.

            if del_or_mod == 'x':
                break

            elif del_or_mod == 'm':         # Редактируем

                while True:
                    ask_key = (input(mmsg['ASK']['KEY'])).lower()  # Спрашиваем, что именно будем редактировать

                    if ask_key == 'x':
                        break

                    elif ask_key == 'tags':                        # Отдельно прописываем обработку тегов
                        new_tags = list(set((input(mmsg['ASK']['TAGS'])).lower().split(' ')))

                        if new_tags == 'x': break

                        mcontacts[detect_id][ask_key] = new_tags
                        mcontacts[detect_id]['modified'] = get_formated_datetime()  # Фиксируем время изменения
                        s_json(mcont_path, mcontacts)

                    elif ask_key in mcontacts[detect_id] and ask_key != 'tags':
                        ask_new_item = input(mmsg['ASK']['ITEM'])

                        if ask_new_item == 'x': break

                        mcontacts[detect_id][ask_key] = ask_new_item
                        mcontacts[detect_id]['modified'] = get_formated_datetime()
                        s_json(mcont_path, mcontacts)

                        print(mmsg['SYS']['MODIFY_OK'].format(detect_id=detect_id))

                    else:
                        print(mmsg['SYS']['FIELD_ERR'])

            elif del_or_mod == 'd':  # Удалить контакт

                while True:
                    del_confirm = input(mmsg['ASK']['CONFIRM_DEL']).lower()

                    if del_confirm == 'y':

                        del mcontacts[detect_id]
                        s_json(mcont_path, mcontacts)
                        print(mmsg['SYS']['DEL_OK'].format(detect_id=detect_id))
                        break

                    elif del_confirm == 'n':
                        break

                    else:
                        print(mmsg['SYS']['IN_ERR'])

            else:
                print(msg_eng['SYS']['IN_ERR'])

        else:
            print(msg_eng['SYS']['ID_ERR'])


def search_(string, secontacts):

    found_contacts = {}
    for c_id, contact in secontacts.items():
        for item in contact.values():
            if string in (str(item)).lower():
                found_contacts[c_id] = secontacts[c_id]

    if not found_contacts: return False

    else: return found_contacts

if __name__ == "__main__":
    print(create_contact(msg_eng))