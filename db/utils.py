import psycopg2
import yaml
import os


def connect():
    config = {}
    yml_path = os.path.join(os.path.dirname(__file__),'../config/cred.yml')
    with open(yml_path, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return psycopg2.connect(dbname=config['database'],
                            user=config['user'],
                            password=config['password'],
                            host=config['host'],
                            port=config['port'])

def exec_file(path):
    full_path = os.path.join(os.path.dirname(__file__),f'{path}')
    con = connect()
    cur = con.cursor()
    with open(full_path, 'r') as file:
        cur.execute(file.read())
    con.commit()
    con.close()

def commit(sql, args={}):
    con = connect()
    cur = con.cursor()
    res = cur.execute(sql, args)
    con.commit()
    con.close()
    return res