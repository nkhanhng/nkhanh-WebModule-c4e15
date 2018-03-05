from flask import Flask, render_template
from models.customer import Customer

import mlab

mlab.connect()

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/customer')
def customer():
    all_customers = Customer.objects()
    return render_template('all_customer.html',all_customers = all_customers)

@app.route('/male')
def male():
    male_customer = Customer.objects(gender=1)[:10]
    return render_template('male_customer.html',male_customer=male_customer)

if __name__ == '__main__':
  app.run(debug=True)
