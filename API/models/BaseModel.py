#!/usr/bin/python
# -*- coding:utf-8 -*-
# BaseModel python file 

from sqlalchemy import *

engine = create_engine("mysql+mysqldb://root:aruba@localhost/webapp")

engine.echo = True

metadata = MetaData(bind=engine)

userdetails = Table("userdetails", metadata, autoload=True)

def login_auth(username, password):
    stm = userdetails.select(and_(userdetails.c.Name == username, userdetails.c.Password == password))
    result = stm.execute()
    if result.rowcount > 0:
       return True
    else:
        return False
