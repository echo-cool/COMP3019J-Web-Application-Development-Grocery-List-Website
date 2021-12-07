# -*- coding: utf-8 -*-
"""User views."""
import os
from urllib import request

from flask import Blueprint, render_template, flash, redirect, url_for, current_app, Response
from sqlalchemy.util import FacadeDict

from project import db
from project.models.UserModel import User
from project.user.forms import UpdateUser
from project.utils import flash_errors, login_required, logout_user, get_current_user, admin_required

blueprint = Blueprint("admin", __name__, static_folder="../static")


@blueprint.route('/admin/view')
@login_required
@admin_required
def view_all_tables() -> Response:
    data: FacadeDict = db.metadata.tables
    return render_template('admin/view.html', tables=data, current_user=get_current_user())


@blueprint.route('/admin/view/<string:table_name>')
@login_required
@admin_required
def view_table_details(table_name: str) -> Response:
    data = db.session.query(db.metadata.tables[table_name]).all()
    print(data)
    return render_template('admin/data.html', data=data, current_user=get_current_user())


@blueprint.route('/admin/del_table/<string:table_name>')
@login_required
@admin_required
def del_table_data_by_name(table_name: str) -> Response:
    db.session.query(db.metadata.tables[table_name]).delete()
    db.session.commit()
    data = db.session.query(db.metadata.tables[table_name]).all()
    flash("Table deleted --- " + table_name)
    return redirect(url_for('admin.view_all_tables'))

@blueprint.route('/admin/del_all_tables')
@login_required
@admin_required
def del_all_table_data() -> Response:
    data: FacadeDict = db.metadata.tables
    for name in data:
        db.session.query(db.metadata.tables[name]).delete()
        db.session.commit()
    logout_user()
    flash("All data deleted")
    return redirect(url_for('admin.view_all_tables'))
