from utils.functions import sign_substitution_from, last_operation_exe, sing_substitution_to
import json

if __name__ == '__main__':
    with open('operations.json' , 'r', encoding='utf-8') as file:
        data = json.load(file)


    for operation in last_operation_exe(data):
        date_operation = operation['date'][6:8] + '.' + operation['date'][4:6] + '.' + operation['date'][0:4]
        description = operation['description']
        if operation.get('from'):
            operation_from = sign_substitution_from(operation['from'])
        else:
            operation_from = ''
        if operation.get('to'):
            operation_to = sing_substitution_to(operation['to'])
        amount = operation['operationAmount']['amount']
        currency_name = operation['operationAmount']['currency']['name']
        print(f'{date_operation} {description}\n'
              f'{operation_from} -> {operation_to}\n'
              f'{amount} {currency_name}\n')
