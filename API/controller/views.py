#!/usr/bin/python
# -*-coding: utf-8 -*-

#from API.controller import view_control
#from API import webapp
from API.models import BaseModel
from flask import request, render_template, flash
from flask import Blueprint

view_control = Blueprint('view_control', 'controller', template_folder="../../template")

@view_control.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")


@view_control.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if BaseModel.login_auth(request.form["username"], request.form["password"]):
           return render_template("home.html")
        else:
            flash("Login Failed")
            return render_template('login.html')
