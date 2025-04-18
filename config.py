#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7415375659:AAFjS6TkbM9Slqvj_MgXThYGoo_p7WhdKtk")
    API_ID = int(os.environ.get("API_ID", "26741193"))
    API_HASH = os.environ.get("API_HASH", "d6edb2646c502e9640c98f75a7214a5a")
    AUTH_USERS = "7356743935"

