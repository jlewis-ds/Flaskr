# -*- coding: utf-8 -*-
"""
DATABASE

Created on Mon May 27 11:55:04 2019

@author: jlewis
"""

import sqlite3

import pandas as pd
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
                )
        g.db.row_factory = sqlite3.Row
        
        tbs = g.db
        print(pd.read_sql_query('SELECT * FROM user', con=tbs))
        
    return g.db
    
def close_db(e=None):
    db = g.pop('db', None)
    
    if db is not None:
        db.close()
        
def init_db():
    db = get_db()
    
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear existing data, make new tables"""
    
    init_db()
    click.echo('Initialized the database')
    
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)