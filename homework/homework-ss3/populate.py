import mlab
from models.service import Service
from faker import Faker
from random import randint,choice

mlab.connect()

fake = Faker()

# http://bit.ly/webc3girl1
# http://bit.ly/webc3girl2
# http://bit.ly/webc3girl3
# http://bit.ly/webc3girl4
# http://bit.ly/webc3girl5
# http://bit.ly/webc3girl6
# http://bit.ly/webc3girl7
# http://bit.ly/webc3girl8
# http://bit.ly/webc3girl9
character1 = ["Thich mao hiem","Tu tin","Kheo tay","Tinh te"]
character2 = ["Duyen dang","Hai huoc","Dang yeu","Nhe nhang"]
character3 = ["Bi an","Diu dang","Chung thuy","Doc lap"]

for i in range(9):
    print("Saving service ",i+1,'.....')
    service = Service(name = fake.name(),
                      yob = randint(1990,2000),
                      gender = randint(0,1),
                      height = randint(140,180),
                      phone = fake.phone_number(),
                      address = fake.address(),
                      status = choice([True,False]),
                      image = "http://bit.ly/webc3girl{0}".format(i+1),
                      description = choice(character1) + "," + choice(character2) +
                                     "," + choice(character3),
                      measurements = [randint(75,85),randint(55,65),randint(75,85)])

    service.save()
