from mysql.connector import connect, Error
from transliterate import translit

from misc.constants import *


class MySQLClient:

    def __init__(self):
        self.host = 'localhost'
        self.database = 'mireadg'

        self.user = 'datagrip'
        self.password = 'password'

        self._connection = None

    def __enter__(self):
        self._connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()

    def _connect(self):
        try:
            self._connection = connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except Error as e:
            raise e

    def query(self, query, mode, get_original_column_names=False):
        if mode not in QueryModes:
            raise ValueError('invalid query mode')

        with self._connection.cursor() as cursor:
            cursor.execute(query)

            match mode:
                case QueryModes.GET:
                    entries = tuple(cursor.fetchall())
                    columns = tuple(self.format_column_name(name) for name in cursor.column_names)

                    if get_original_column_names:
                        return columns, entries, cursor.column_names
                    else:
                        return columns, entries

                case QueryModes.GET_PRIMARY_KEY:
                    entries = cursor.fetchall()
                    return entries[0][4]

        if mode == QueryModes.EDIT:
            self._connection.commit()

    @staticmethod
    def format_column_name(field: str):
        transliteration: str = translit(field.replace('_', ' '), 'ru')

        transliteration = transliteration.replace('цт', 'тст')
        transliteration = transliteration.replace('лн', 'льн')
        transliteration = transliteration.replace('лг', 'льг')
        transliteration = transliteration.replace('Лг', 'Льг')
        transliteration = transliteration.replace('сч', 'щ')
        transliteration = transliteration.replace('еле', 'эле')
        transliteration = transliteration.replace('ост', 'ость')
        transliteration = transliteration.replace('тэ', 'те')
        transliteration = transliteration.replace('тьа', 'та')
        transliteration = transliteration.replace('ишо', 'исхо')

        return transliteration
