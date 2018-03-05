import mlab
from models.service import Service

mlab.connect()

all_services = Service.objects()

all_services.delete()
