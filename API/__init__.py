#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, session

#--App Configuration--#
webapp = Flask("API", static_folder="../static", template_folder="../template")
webapp.config.from_object('API.config')

import API.core
import API.controller
import API.models
