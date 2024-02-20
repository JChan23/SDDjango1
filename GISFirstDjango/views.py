from django.shortcuts import render
from .models import Person

def splash(request):
    name = 'Billy'
    lst = ['Cat', 'Dog', 'Mouse', 'Monkey', 'Bird']
    people = Person.objects.all()
    debug_people = list(people)
    return render(request, "splash.html", {'name': name,'lst':lst})