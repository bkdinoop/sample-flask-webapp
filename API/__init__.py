#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, session
from API.controller.views import view_control

#--App Configuration--#
webapp = Flask("API", static_folder="../static", template_folder="../template")
webapp.register_blueprint(view_control)
webapp.config.from_object('API.config')

import API.core
import API.controller
import API.models
