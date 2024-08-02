"""{{ cookiecutter.project_name }}."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
#

from {{ cookiecutter.project_slug }} import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
