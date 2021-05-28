from flask import Flask, render_template, redirect, url_for, flash, request, send_from_directory
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,RadioField,SelectField,BooleanField,TextField,fields
from wtforms.validators import DataRequired
from flask import send_file
from werkzeug.utils import secure_filename
import os
import subprocess
from wtforms.widgets import TextArea
import os
from optparse import OptionParser
import json


from url_check_main import URL_Check

app = Flask(__name__,static_folder='assets',)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

Bootstrap(app)

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class InfoForm(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''
    #breed = StringField('What breed are you?')
    url = StringField('Enter the URL to be Validated', validators=[DataRequired()],render_kw={"placeholder": "Provide the URL which needs to be be validated"})
    submit = SubmitField('Validate URL')

def process_forma_values(url):
    #url = "cricinfo.com"

    result = {}
    urlcheckinst = URL_Check(url)
    validity, url_failed = urlcheckinst.url_verify()
  
    if validity and not url_failed:
        result[url] = f"The Given URL is Clean - {url}"
    elif not validity and not url_failed:
        result[url] = f"The Given URL is Malware Affected - {url}"
    elif url_failed:
        result[url] = f"The Given URL is Not in Valid URL Format - {url}"

    print(json.dumps(result))
    return(json.dumps(result))

@app.route('/', methods=['GET', 'POST'])
def url_d():
    form = InfoForm()
    output = ""
    if request.method == 'POST':
        form = InfoForm()
        message = ""
        if form.validate_on_submit():
            url = form.url.data
            output = process_forma_values(url)
            form.url.data = ''
    return render_template('home.html', form=form, analysis=output)

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=5001)

