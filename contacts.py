from prettytable import PrettyTable


def list_(lcontacts):

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

    for i, (cid, info) in enumerate(lcontacts.items(), start=1):

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


def show_one_(scontacts,detect_id):

    print(f'\nID: {detect_id}, {scontacts[detect_id].get("created", "N/A")}')
    print(f'Name/Nickname : {scontacts[detect_id].get("name", "N/A")}')
    print(f'Surname       : {scontacts[detect_id].get("surname", "N/A")}')
    print(f'Phone number  : {scontacts[detect_id].get("phone", "N/A")}')
    print(f'Comment   : {scontacts[detect_id].get("comment")}')
    print(f'Tags : {scontacts[detect_id].get("tags", "N/A")}')
    print('---')


def options_menu(omsg):

    print(omsg['OPT']['TITLE_'])
    print(omsg['OPT']['LIST_A'])
    print(omsg['OPT']['ADDNEW'])
    print(omsg['OPT']['SEARCH'])
    print(omsg['OPT']['X'])



def search_(secontacts, string):

    found_contacts = {}
    for c_id, contact in secontacts.items():
        for item in contact.values():
            if string in (str(item)).lower():
                found_contacts[c_id] = secontacts[c_id]

    if not found_contacts: return False

    else: return found_contacts

# if __name__ == "__main__":
   # print(create_contact(msg_eng))