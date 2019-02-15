import os

from flask import Flask, render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )     
    
    @app.route('/about')
    def input_form():        
        return render_template("about.html")
    
    from . import main
    app.register_blueprint(main.bp)

    return app


