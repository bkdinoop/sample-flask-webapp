#!/usr/bin/python
# -*- coding: utf-8 -*-
# Flask Web Object
# runserver.py

import os
from API import webapp

if __name__ == "__main__":
   webapp.run('0.0.0.0', port=8000)
