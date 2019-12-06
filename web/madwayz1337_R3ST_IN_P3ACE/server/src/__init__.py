from flask import Flask

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = 'DB3XbhrRnvUILOo_igUfg'

import src.views