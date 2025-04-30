msg_eng = {

    'OPT' : {

        'TITLE_'         : "\n--- Options ---",
        'LIST_A'         : "[1] View all contacts",
        'ADDNEW'         : "[2] Add new contact",
        'SEARCH'         : "[3] Search contact",
        'DETECT_ID'      : "\nEnter contact ID number to modify/delete or [x] to go back to options: ",
        'MODIFY'         : "[1] Modify contact",
        'DELETE'         : "[2] Delete contact",
        'SELECT'         : "\nSelect option: ",
        'X'              : "[x] Exit",
        'BYE'            : "Contacts-cli is now closed",
        'SEARCH_MENU'    : "Insert string for global search or [x] to cancel",

        'SEARCH_HELP'   :

"""
-Add '/' to search in particular fields.
 Example | Search: /name Alex""",

    },

    'INI' : {

        'LANG_CHECK'    : "English",
        'FIRST_RUN'     : "Welcome to Contacts-CLI! This is the first run.",
        'HELLO_'        : "\nWelcome to Contacts-CLI!",
        'SYS_LANG'      : "Select user language (RU/EN): ",
        'EN_OK'         : "English language is selected",
        'FST_CONT'      : "Let's create you first contact!",
    },

    'ASK' : {
        'TELE'          : "\nEnter phone number or [x] to cancel: ",
        'NAME'          : "Enter name: ",
        'SURN'          : "Enter surname: ",
        'NOTE'          : "Enter any additional notes: ",
        'TAGS'          : "Enter tags, separated by spaces: ",
        'ADDC'          : "Would you like to add one more field? [Y]/[n]: ",
        'DEL_OR_MOD'    : "Press [m] to modify, or [d] to delete, or [x] to cancel: ",
        'KEY'           : "Enter field to modify or [x] to cancel: ",
        'ITEM'          : "Enter new value or [x] to cancel: ",
        'CONFIRM_DEL'   : "Are you sure you want to delete this contact? [Y]/[n]: ",
    },

    'SYS' : {

        'IN_ERR'        : "Input error, please try again!",
        'IN_ERR_L'      : "Input error! Please try again, or press \"Enter\" to use eng!",
        'ID_ERR'        : "No such ID found! Please try again",
        'LANG_ERR'      : "Unknown language",
        'CONF_ERR'      : "Unknown setting arguments, check settings.json!",
        'FIELD_ERR'     : "No such a field! Please try again.",
        'MODIFY_OK'     : "Contact {detect_id} was updated successfully!",
        'DEL_OK'        : "Contact {detect_id} was deleted successfully!",
        'NOT_FOUND'     : "Nothing found!"
    },


}

msg_ru = {

    'OPT': {
        'TITLE_': "\n--- Опции ---",
        'LIST_A': "[1] Показать все контакты",
        'ADDNEW': "[2] Добавить новый контакт",
        'SEARCH': "[3] Поиск контакта",
        'DETECT_ID': "\nВведите ID контакта для изменения/удаления или [x] для возврата в меню: ",
        'MODIFY': "[1] Изменить контакт",
        'DELETE': "[2] Удалить контакт",
        'SELECT': "\nВыберите опцию: ",
        'X': "[x] Выход",
        'BYE': "Контакт-CLI завершил работу",
        'SEARCH_MENU': """
Введите строку для глобального поиска.
[x] Отмена""",
        'SEARCH_HELP': """
-Добавьте '/' для поиска по определённым полям.
 Пример | Поиск: /name Алексей""",
    },

    'INI': {
        'LANG_CHECK': "Русский",
        'FIRST_RUN': "Добро пожаловать в Contacts-CLI! Это первый запуск.",
        'HELLO_': "\nДобро пожаловать в Contacts-CLI!",
        'SYS_LANG': "Выберите язык пользователя (RU/EN): ",
        'EN_OK': "Выбран русский язык",
        'FST_CONT': "Давайте создадим ваш первый контакт!",
    },

    'ASK': {
        'TELE': "Введите номер телефона или [x] для отмены: ",
        'NAME': "Введите имя: ",
        'SURN': "Введите фамилию: ",
        'NOTE': "Введите дополнительные заметки: ",
        'TAGS': "Введите теги через пробел: ",
        'ADDC': "Хотите добавить ещё одно поле? [Y]/[n]: ",
        'DEL_OR_MOD': "Нажмите [m] для изменения, [d] для удаления или [x] для отмены: ",
        'KEY': "Введите поле для изменения или [x] для отмены: ",
        'ITEM': "Введите новое значение или [x] для отмены: ",
        'CONFIRM_DEL': "Вы уверены, что хотите удалить этот контакт? [Y]/[n]: ",
    },

    'SYS': {
        'IN_ERR': "Ошибка ввода, попробуйте ещё раз!",
        'IN_ERR_L': "Ошибка ввода! Повторите попытку или нажмите \"Enter\" для выбора английского языка!",
        'ID_ERR': "Контакт с таким ID не найден! Попробуйте ещё раз",
        'LANG_ERR': "Неизвестный язык",
        'CONF_ERR': "Неизвестные параметры конфигурации, проверьте settings.json!",
        'FIELD_ERR': "Такого поля нет! Повторите попытку.",
        'MODIFY_OK': "Контакт {detect_id} успешно обновлён!",
        'DEL_OK': "Контакт {detect_id} успешно удалён!",
        'NOT_FOUND': "Ничего не найдено",
    },
}
