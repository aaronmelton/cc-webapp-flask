# !/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def print_instructions():
    print("")
    print("Run these commands to complete project creation:")
    print("1. cd {{ cookiecutter.project_name }}")
    print("2. poetry shell")
    print("3. poetry update")
    print("")

if __name__ == '__main__':
    print_instructions()