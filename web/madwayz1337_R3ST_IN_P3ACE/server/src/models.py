from psycopg2.extras import RealDictCursor
from os import environ
from sys import stderr
import psycopg2

class db:
    @staticmethod
    def __execute(query):
        """ Метод для выполнения SQL запросов """

        try:
            conn = psycopg2.connect(
                dbname=environ.get('POSTGRES_DB'),
                user=environ.get('POSTGRES_USER'),
                host=environ.get('POSTGRES_HOST'),
                port=5432
            )

            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute(query)
            conn.commit()

            answer = None
            try:
                answer = cursor.fetchall()
                print('SQL answ:', answer, file=stderr)
            except psycopg2.Error as err:
                print(err, file=stderr)
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
                return answer

        except psycopg2.OperationalError as err:
            print('PostgreSQL ERR:', err, file=stderr)
            return dict(error=dict(message="Database connection refused"))

    @classmethod
    def get_users(cls):
        """ Получение всех юзеров """

        users = {'users': []}
        query="select id, login, first_name, last_name, algorithm from users"
        response = cls.__execute(query)

        # if isinstance(response, dict):
        if type(response) == dict:
            return {'error': {'message': 'Whoops! Some problems with database.'}}

        for userdata in response:
            users['users'].append(dict(userdata))

        return users

    @classmethod
    def update_users(cls, ID, token):
        """ Обновление данных юзера по ID"""
        query=f"update users set token='{token}' where id={ID}"
        cls.__execute(query)

    @classmethod
    def get_user(cls, HASH_USERID):
        """ Получение юзера по ID """

        query=f"select id, login, token, first_name, last_name from users where hash_id='{HASH_USERID}'"
        return cls.__execute(query)

    @classmethod
    def get_id(cls, HASH_USERID):
        """ Получение юзера по ID """
        query = f"select id from users where hash_id='{HASH_USERID}'"
        return cls.__execute(query)

    @classmethod
    def insert_users(cls, data):
        """ Добавление пользователей в базу """

        query="insert into users (login, token) values ('{login}', '{token}');".format(**data)
        cls.__execute(query)
