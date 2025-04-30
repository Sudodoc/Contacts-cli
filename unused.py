# elif s_string.startswith('/'):
#
# search_list = s_string[1:].split(' ')
#
# print(search_list)
#
# found_contacts = {}
#
# for c_id in contacts.keys():
#
#     if search_list[0] in contacts[c_id]:
#         print('yes')
#         for item in contacts[c_id][search_list[0]]:
#             if s_string in (str(item)).lower():
#                 found_contacts[c_id] = contacts[c_id]
#
#         print(found_contacts)
#         list_(found_contacts)
#         modify_or_delete(msg, contacts, cont_path)
#
#     else:
#         print(msg['SYS']['FIELD_ERR'])