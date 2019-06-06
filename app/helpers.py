import os
import string
import random
import psycopg2

def url_shortner():
    return ''.join(random.choice(string.hexdigits[:15]) for x in range(12))

def get_pastes_num():
    connection = psycopg2.connect(user = os.environ.get('USER'),
                                  password = os.environ.get('PASSWORD'),
                                  host = os.environ.get('HOST'),
                                  port = os.environ.get('DB_PORT'),
                                  database = os.environ.get('NAME'))
    cursor = connection.cursor()
    cursor.execute('''  SELECT username, COUNT(*)
                        FROM  public.app_customuser
                        INNER JOIN public.app_snippet
                        ON public.app_customuser.id = public.app_snippet.owner_id
                        GROUP BY username
                        ;''')
    record = cursor.fetchall()

    cursor.close()
    connection.close()
    return record
