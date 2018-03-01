from flask import Flask, render_template
from models.service import Service

import mlab

mlab.connect()

app = Flask(__name__)


@app.route('/search')
def search():
    service = Service.objects.get(id= "5a95626a65c39a1ff07a69a9")
    return render_template('index.html',service= service)

if __name__ == '__main__':
  app.run(debug=True)
