
from django.contrib import admin
from .models import Person, Education, ProfessionalSkills

# Register your models here.
admin.site.register(Person)
admin.site.register(Education)
admin.site.register(ProfessionalSkills)