#! /usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
sys.path.append(os.path.abspath(".."))
from main import RT10yy_main

class secBootRTxxxUi(RT10yy_main.secBootRT10yyMain):

    def __init__(self, parent):
        RT10yy_main.secBootRT10yyMain.__init__(self, parent)

