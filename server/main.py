import traceback

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():    
    return redirect(url_for('main.input_form'))

@bp.route('/input_form')
def input_form():        
    return render_template("input_form.html")
    
@bp.route('/fixer', methods=('GET', 'POST'))
def fixer():
    bibtex = None
    if request.method == 'POST': # form sent
        
        form = request.form
        
        if not "bibtex_input" in form:
            flash("No BibTeX given.", "warning")
        else:
            bibtex = form["bibtex_input"]
        
        if "option_uppercase" in form and form["option_uppercase"] == "True":
            bibtex = bibtex.upper()
        
        if not bibtex is None:
            flash("BibTex fixed", "success")
            
    return render_template("input_form.html", bibtex=bibtex)
