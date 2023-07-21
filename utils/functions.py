import re
from operator import itemgetter
def sign_substitution_from(account_from):
    word_list = account_from.split()

    for word in word_list:
        if word.isnumeric():
           digit_account = word
    name_of_account = re.sub('[0-9]', '',account_from)
    a = digit_account[0:4]
    b= digit_account[4:6]
    c = digit_account[12:16]
    sign_substitution_account =name_of_account + a + ' ' + b + '** **** ' + c
    return sign_substitution_account

def last_operation_exe(data):
    operation_exe = []
    for operation in data:
        if operation.get('state') and operation['state'] == "EXECUTED":
            operation_exe.append(operation)
    for operation in operation_exe:
        date = ''
        for element in operation['date']:
            if element.isdigit():
                date = date + element
                operation['date'] = date
            else:
                date = date
    operation_exe.sort(key=itemgetter('date'), reverse=True)

    last_operation_exe = []
    for i in range(1, 6):
        last_operation_exe.append(operation_exe[i])
    return last_operation_exe
def sing_substitution_to(account_to):
    word_list = account_to.split()

    for word in word_list:
        if word.isnumeric():
            digit_account = word
        elif word.isnumeric() != True:
            name_of_account = word
    c = digit_account[16:20]
    sign_substitution_account = name_of_account + ' ' '**' + c
    return sign_substitution_account