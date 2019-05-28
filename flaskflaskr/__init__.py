# -*- coding: utf-8 -*-
"""
FLASKR - init

Created on Mon May 27 09:54:06 2019

@author: jlewis
"""

import os

from flask import Flask

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskflaskr.sqlite'),
            )
    
    if test_config is None:
        #load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    #simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello!'
    
    from . import db, auth, blog
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app