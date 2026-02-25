import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crud_project.settings') #path
import django
django.setup()

from crud_app.models import * #myapp
from faker import Faker #module 
from random import * #random module
faker=Faker()

def generate(n):
    for i in range(n):
        fsno=randint(1,1000)
        fsname=faker.name()
        fsclass=randint(1,10)
        fsaddress=faker.city()
        std_record=Student.objects.get_or_create(sno=fsno,sname=fsname,sclass=fsclass,saddress=fsaddress)
generate(20)

#python manage.py runserver