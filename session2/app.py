from flask import Flask, render_template

from models.service import Service
import mlab

mlab.connect()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    services = Service.objects(gender=gender,yob__lte=1998,height__gte=160,address__iexact='ha noi')
    return render_template('search.html', all_services = services)


if __name__ == '__main__':
  app.run(debug=True)
