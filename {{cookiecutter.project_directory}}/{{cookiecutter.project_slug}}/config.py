"""{{ cookiecutter.project_name }} Config."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
#

from dataclasses import dataclass
from datetime import datetime
from os import environ as os_environ


@dataclass
class Config:  # pylint: disable=too-many-instance-attributes
    """Class for Application variables."""

    def __init__(self):
        """Application Variables."""
        self.app_dict = {
            "author": "{{ cookiecutter.author }}",
            "date": "{{ cookiecutter.project_date }}",
            "desc": "{{ cookiecutter.project_description }}",
            "title": "{{ cookiecutter.project_slug }}",
            "url": "{{ cookiecutter.project_url }}",
            "version": "{{ cookiecutter.version }}",
        }

        # Azure Variables
        self.az_app_dict = {
            "client_id": os_environ.get("AZ_CLIENT_ID", None),
            "client_secret": os_environ.get("AZ_CLIENT_SECRET", None),
            "tenant_id": os_environ.get("AZ_TENANT_ID", None),
            "authority": f"""https://login.microsoftonline.com/{os_environ.get("AZ_TENANT_ID", "common")}""",
            "redirect_path": "/getAToken",
            "endpoint": "https://graph.microsoft.com/v1.0/users",
            "scope": ["User.ReadBasic.All"],
            "session_type": "filesystem",
        }

        # Logging Variables
        self.log_dict = {
            "filename": f"""{os_environ.get("LOG_PATH", "./log/")}{self.app_dict["title"]}_{datetime.now().strftime("%Y%m%d")}.log""",
            "level": os_environ.get("LOG_LEVEL", "INFO"),
            "path": os_environ.get("LOG_PATH", "./log/"),
        }

        # API Keys
        self.key_dict = {
            "api_key": os_environ.get("API_KEY", None),
        }
