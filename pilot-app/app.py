from flask import *
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

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html',all_services = services)

@app.route('/delete/<service_id>')
def delete(service_id):
    #del_service = Service.objects().with_id(service_id)
    del_service = Service.objects.get(id = service_id)
    del_service.delete()
    return redirect(url_for('admin'))

@app.route('/new_service',methods = ['GET','POST'])
def creat():
    if request.method == 'GET':
        return render_template('new_service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']

        new_service = Service(name = name,
                              yob = yob,
                              phone = phone,
                              gender = 1,
                              height = 170,
                              address = 'Ha Noi',
                              status = True)
        new_service.save()
        return "Saved"

if __name__ == '__main__':
  app.run(debug=True)
