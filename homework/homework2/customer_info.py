import mlab
from models.customer import Customer
from faker import Faker
from random import randint,choice

mlab.connect()

fake = Faker()

for i in range(100):
    print("Saving customer", i + 1,'.....')
    customer = Customer(name = fake.name(),
                        gender = randint(0,1),
                        email = fake.free_email(),
                        phonenumber = fake.phone_number(),
                        job = fake.job(),
                        company = fake.company(),
                        contacted = choice([True,False]))

    customer.save()
