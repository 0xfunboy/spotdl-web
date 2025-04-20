from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='web/templates', static_folder='web/static', static_url_path='/web/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/web/static/<path:path>') 
def send_static(path):
    return send_from_directory('web/static', path) 

if __name__ == '__main__':
    app.run(debug=True)
