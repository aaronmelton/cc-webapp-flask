"""{{ cookiecutter.project_name }}."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
#

import identity
import identity.web
from flask import (
    Blueprint,
    current_app,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from {{ cookiecutter.project_slug }}.config import Config

config = Config()
home = Blueprint("home", __name__)


auth = identity.web.Auth(
    session=session,
    authority=config.az_app_dict["authority"],
    client_id=config.az_app_dict["client_id"],
    client_credential=config.az_app_dict["client_secret"],
)


@home.route("/about")
def about():
    """Display Application Variables.

    Returns:
        render_template (str): HTML for About button
    """
    current_app.logger.info("Clicked About Button")
    return render_template(
        "about.html",
        app_author=current_app.config["APP_DICT"]["author"],
        app_date=current_app.config["APP_DICT"]["date"],
        app_desc=current_app.config["APP_DICT"]["desc"],
        app_title=current_app.config["APP_DICT"]["title"],
        app_url=current_app.config["APP_DICT"]["url"],
        app_version=current_app.config["APP_DICT"]["version"],
    )


@home.route(config.az_app_dict["redirect_path"])
def auth_response():
    """Auth.

    Args:
        config.az_app_dict (str): GetToken path.

    Returns:
        render_template (str): HTML for Auth button
    """
    result = auth.complete_log_in(request.args)
    if "error" in result:
        return render_template("auth_error.html", result=result)
    return redirect(url_for("home.main"))


@home.route("/get_changelog")
def get_changelog():
    """Read contents of CHANGELOG.md into variable.

    Returns:
        changelog_new (str): Return CHANGELOG.md.
    """
    current_app.logger.info("Clicked Changelog Button")
    changelog_new = ""
    try:
        changelog_file = "CHANGELOG.md"
        with open(changelog_file, "r", encoding="utf-8") as filename:
            current_app.logger.debug("Opened: %s", changelog_file)
            changelog = filename.read()
            changelog = changelog.splitlines()
            for _, value in enumerate(changelog):
                changelog_new += value
                changelog_new += "<br>"
            filename.close()
        current_app.logger.debug("")
    except Exception as some_exception:  # pylint: disable=broad-except
        current_app.logger.error("ERROR==%s", some_exception)
        current_app.logger.error("Error opening: %s", changelog_file)
    return changelog_new


@home.route("/login")
def login():
    """Login.

    Returns:
        render_template (str): HTML for Login
    """
    return render_template(
        "login.html",
        version=identity.__version__,
        **auth.log_in(
            scopes=config.az_app_dict["scope"],
            redirect_uri=url_for("home.auth_response", _external=True),
        )
    )


@home.route("/logout")
def logout():
    """Logout.

    Returns:
        redirect (str): Redirect URL
    """
    # return redirect(auth.log_out(url_for("index", _external=True)))
    return redirect(auth.log_out(url_for("home.main", _external=True)))


@home.route("/", methods=["GET", "POST"])
def main():
    """Start application.

    Args:
        methods (str):

    Returns:
        render_template (str): HTML
    """
    current_app.logger.info("Clicked Home Button")
    if request.method == "GET":
        return render_template(
            "print_this.html",
            print_this="Hello World",
            app_author=current_app.config["APP_DICT"]["author"],
            app_date=current_app.config["APP_DICT"]["date"],
            app_desc=current_app.config["APP_DICT"]["desc"],
            app_title=current_app.config["APP_DICT"]["title"],
            app_url=current_app.config["APP_DICT"]["url"],
            app_version=current_app.config["APP_DICT"]["version"],
        )

    if request.method == "POST":
        return render_template(
            "about.html",
            app_author=current_app.config["APP_DICT"]["author"],
            app_date=current_app.config["APP_DICT"]["date"],
            app_desc=current_app.config["APP_DICT"]["desc"],
            app_title=current_app.config["APP_DICT"]["title"],
            app_url=current_app.config["APP_DICT"]["url"],
            app_version=current_app.config["APP_DICT"]["version"],
        )
    return True
