import mlab
from models.service import Service

mlab.connect()

# all_services = Service.objects()
#
# first_service = all_services[0]
#
# print(first_service.name)

id_to_find = '5a95626665c39a1ff07a699d'

belly = Service.objects().with_id(id_to_find)

print(belly.to_mongo())

if belly is not None:
    # belly.delete()
    belly.update(set__status = True)
    belly.reload()
    print(belly.to_mongo())
else:
    print('Not found')
