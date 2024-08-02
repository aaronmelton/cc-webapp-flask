# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Borrowed from https://github.com/tedivm/robs_awesome_python_template/blob/main/hooks/pre_gen_project.py

import sys
from re import match as re_match


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
module_name = '{{ cookiecutter.project_slug }}'

if not re_match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)

    #Exit to cancel project
    sys.exit(1)