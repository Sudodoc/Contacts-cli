from systems import set_lang
from contclass import ContactList
from msg import msg_eng


def fist_run_ini():

    """
    Функция 'FIRST RUN' - инициализация программы при первом запуске

    - Задаем first_run_ini как False.
    - Устанавливаем язык интерфейса.
    - Создаем первый контакт.
    - Задаем count=1, суммарное кол-во когда бы то ни было созданных контактов).
    - Сохраняем файлы settings.json и contacts.json
    """

    isettings = {}
    imsg = msg_eng

    print(msg_eng['INI']['FIRST_RUN'])
    isettings['fist_run_ini'] = False


    while True:
        lang = (input(msg_eng['INI']['SYS_LANG'])).lower()

        if not lang or lang == 'en':
            isettings['language'] = set_lang()
            break

        elif lang == 'ru':
            isettings['language'], msg = set_lang('ru')
            break

        else:
            print(msg_eng['SYS']['IN_ERR_L'])

    print(imsg['INI']['FST_CONT'])

    contact = ContactList({}, isettings, imsg)
    fst_contact = contact.new()

    isettings['counter'] = 1

    return isettings, imsg, fst_contact

