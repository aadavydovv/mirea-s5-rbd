import decimal
from decimal import Decimal

SELECT_ALL_FROM = 'select * from'


def primary_key_by_table(table):
    return f"SHOW KEYS FROM {table} WHERE Key_name = 'PRIMARY'"


def delete_entry_from_table(table, name_of_primary_key, value_of_primary_key):
    if not (isinstance(value_of_primary_key, int) or isinstance(value_of_primary_key, float)):
        value_of_primary_key = f"'{value_of_primary_key}'"

    query = f"delete from {table} where {name_of_primary_key} = {value_of_primary_key}"
    print(f'delete q: {query}')
    return query


def add_entry_to_table(table, fields, values):
    print(f'values add: {values}')

    fields_as_str = str(fields).replace("'", "")
    query = f"insert into {table} {fields_as_str} values ("

    for n in range(len(fields)):
        value = format_value_for_db(values[n])
        query += f'{value}'

        if n < (len(fields) - 1):
            query += ', '
        else:
            query += ')'

    print(f'add q: {query}')
    return query


def update_entry_in_table(table, fields, values, name_of_primary_key, value_of_primary_key):
    print(f'values update: {values}')
    query = f"update {table} set "

    amount_of_fields = len(fields)
    for n in range(amount_of_fields):
        value = format_value_for_db(values[n])
        query += f'{fields[n]}={value}'

        if n < amount_of_fields - 1:
            query += ','

        query += ' '

    query += f'where {name_of_primary_key}={value_of_primary_key}'

    print(f'update q: {query}')
    return query


def format_value_for_db(value: str):
    if value == '':
        return 'NULL'

    if value == 'True':
        return True

    if value == 'False':
        return False

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return str(Decimal(value)).replace("'", '')
    except decimal.InvalidOperation:
        pass

    # value_split = value.split('-')
    # if len(value_split) > 2:
    #     if value[-1] == '"':
    #         value = value.replace('"', '')
    #     if value[-1] != "'":
    #         value = f"'{value}'"

    return f"'{value}'"
