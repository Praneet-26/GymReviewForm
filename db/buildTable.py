import os
from db.utils import *

def build_Tables():
    exec_file('sql/createTable.sql')
