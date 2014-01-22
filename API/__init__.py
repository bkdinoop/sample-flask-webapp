#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask

#--App Configuration--#
webapp = Flask("API", static_folder="../static", template_folder="../template")

import API.core
import API.controller
import API.models
