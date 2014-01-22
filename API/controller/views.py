#!/usr/bin/python
# -*-coding: utf-8 -*-

@webapp.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
