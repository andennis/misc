#!/usr/bin/python
import os
from configparser import ConfigParser
import psycopg2
import json
from functools import lru_cache


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def add_ping_log(data):
    if not data:
        return
    conn = None
    try:
        conn = _connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO ping_log (log) VALUES (%s);", [json.dumps(data)])
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def get_log(rows_number):
    conn = None
    try:
        conn = _connect()
        cur = conn.cursor()
        cur.execute("select log from ping_log order by id desc LIMIT %s;", [rows_number])
        return [r[0] for r in cur.fetchall()]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def _connect():
    params = _config()
    print('Connecting to the database...')
    return psycopg2.connect(**params)


@lru_cache(maxsize=None)
def _config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(os.path.join(__location__, filename))

    db_config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db_config
