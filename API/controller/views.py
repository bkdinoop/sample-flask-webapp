#!/usr/bin/python
# -*-coding: utf-8 -*-

from API import webapp
from flask import request, render_template

@webapp.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")


@webapp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        return (request.form["username"], request.form["password"])
