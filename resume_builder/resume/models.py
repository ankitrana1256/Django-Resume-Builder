from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm


class Person(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return " ".join([self.first_name, self.last_name])


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'gender', 'age', 'mobile',
                  'address', 'email', 'github', 'linkedin')


class Education(models.Model):
    DEGREE_CHOICES = (
        ('Phd', 'Phd'),
        ('Mtech/MA/MSc/MCom/MBA', 'Mtech/MA/MSc/MCom/MBA'),
        ('BE/Btech/BA/BSc/BCom', 'BE/Btech/BA/BSc/BCom'),
        ('12th', '12th')
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)
    stream = models.CharField(max_length=100)
    description = models.TextField()


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ('degree', 'stream', 'description')


class ProfessionalSkills(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    skill_detail = models.TextField()


class ProfessionalSkillsForm(ModelForm):
    class Meta:
        model = ProfessionalSkills
        fields = ('skill_detail',)


