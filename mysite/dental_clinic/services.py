from django.db import connection
from contextlib import closing


def get_services():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from service""")
        services = dict_fetchall(cursor)
        return services


def get_testimonials():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from testimonial""")
        testimonials = dict_fetchall(cursor)
        return testimonials


def get_doctor():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  * from doctor""")
        doctor = dict_fetchall(cursor)
        return doctor


def get_contact():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from contact""")
        contact = dict_fetchall(cursor)
        return contact


def get_hours():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from opening""")
        hours = dict_fetchall(cursor)
        return hours

def get_price():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from price""")
        price = dict_fetchall(cursor)
        return price

def get_doctor_service():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from doctor_service""")
        doctor_service = dict_fetchall(cursor)
        return doctor_service


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
