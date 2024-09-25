"""Test class Config."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pylint: disable=invalid-name, duplicate-code

from re import match as re_match

from {{ cookiecutter.project_slug }}.config import Config


def test_config():
    """Test config.py"""
    # Application Variables
    config = Config()
    assert config.app_dict["author"] == "{{ cookiecutter.author }}"
    assert re_match("\\d{4}(-\\d{2}){2}", "{{ cookiecutter.project_date }}")
    assert config.app_dict["desc"] == "{{ cookiecutter.project_description }}"
    assert config.app_dict["title"] == "{{ cookiecutter.project_slug }}"
    assert config.app_dict["url"] == "{{ cookiecutter.project_url }}"
    assert re_match("\\d{1,2}(\\.\\d{1,2}){2}", config.app_dict["version"])
