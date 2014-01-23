#!/usr/bin/python
# -*- coding:utf-8 -*-
# BaseModel python file 

from sqlalchemy import *

engine = create_engine("postgresql://admin:@dmin@localhost/webapp")

engine.echo = True

metadata = MetaData(bind=engine)

userdetails = Table("userdetails", metadata, autoload=True)

def login_auth(username, pword):
    stm = userdetails.select(and_(userdetails.c.name == username, userdetails.c.password == pword))
    result = stm.execute()
    if result.rowcount > 0:
       return True
    else:
        return False
