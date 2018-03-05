from flask import *
from models.service import Service
import mlab

mlab.connect()

app = Flask(__name__)


@app.route('/service')
def service():
    all_services = Service.objects()
    return render_template('service.html',all_services = all_services)

@app.route('/detail/<sid>')
def detail(sid):
    service_id = Service.objects.get(id = sid)
    return render_template('detail.html',service = service_id)

@app.route('/new_service',methods = ['GET','POST'])
def creat():
    if request.method == 'GET':
        return render_template('new_service.html',)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        phone = form['phone']
        address = form['address']
        status = form['status']
        image = form['image']
        description = form['description']
        measure1 = int(form['measure1'])
        measure2 = int(form['measure2'])
        measure3 = int(form['measure3'])
        measurements = [measure1,measure2,measure3]

        new_service = Service(name = name,
                              yob = yob,
                              gender = gender,
                              height = height,
                              phone = phone,
                              address = address,
                              status = status,
                              image = image,
                              description = description,
                              measurements = measurements)

        new_service.save()
        return "Saved"

@app.route('/update_service/<service_id>',methods = ['GET','POST'])
def update(service_id):
    update_service = Service.objects.get(id = service_id)

    if request.method == 'GET':
        return render_template("update_service.html",update_service = update_service)
    elif request.method == 'POST':
        print(update_service)
        form = request.form
        name = form['name']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        phone = form['phone']
        address = form['address']
        status = form['status']
        image = form['image']
        description = form['description']
        measure1 = int(form['measure1'])
        measure2 = int(form['measure2'])
        measure3 = int(form['measure3'])
        measurements = [measure1,measure2,measure3]

        update_service.update(set__name = name, set__yob = yob,
                              set__gender = gender,set__height = height,
                              set__phone = phone,
                              set__address = address,
                              set__status = status,set__image = image,
                              set__description = description,
                              set__measurements = measurements)

        return "Saved"
if __name__ == '__main__':
  app.run(debug=True)
