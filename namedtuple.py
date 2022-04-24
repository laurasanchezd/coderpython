from collections import namedtuple
Fish= namedtuple("Fish", ['name','species','tank'])

mi_primerpez= Fish("sammy","tiburon","tanque grande")

print(mi_primerpez)
print(mi_primerpez._asdict()) #lo convierte en un diccionarioport namedtuple
Fish= namedtuple("Fish", ['name','species','tank'])

mi_primerpez= Fish("sammy","tiburon","tanque grande")

print(mi_primerpez)
print(mi_primerpez._asdict()) #lo convierte en un diccionario