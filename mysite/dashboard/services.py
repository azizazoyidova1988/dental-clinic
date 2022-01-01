from django.db import connection
from contextlib import closing


def get_price():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from price""")
        price = dict_fetchall(cursor)
        return price


def get_testimonial():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from testimonial""")
        testimonial = dict_fetchall(cursor)
        return testimonial


def get_testimonial_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from testimonial""")
        testimonial_count = dict_fetchall(cursor)
        return testimonial_count


def get_service():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from service""")
        service = dict_fetchall(cursor)
        return service

def get_doctor():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from doctor""")
        doctor = dict_fetchall(cursor)
        return doctor

def get_service_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from service""")
        service_count = dict_fetchall(cursor)
        return service_count


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
