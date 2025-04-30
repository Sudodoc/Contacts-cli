from systems import set_lang
from contacts import create_contact
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

    fst_contact = create_contact(imsg, 1)
    isettings['counter'] = 1

    return isettings, imsg, fst_contact, 1

