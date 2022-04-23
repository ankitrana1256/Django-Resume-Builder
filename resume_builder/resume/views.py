from django.shortcuts import render
from django.contrib.sites.requests import RequestSite
from .models import Person, Education, ProfessionalSkills, PersonForm, \
    EducationForm, ProfessionalSkillsForm


def resumeFill(request):
    if request.method == 'POST':
        personform = PersonForm(request.POST)
        educationform = EducationForm(request.POST)
        professionalSkillsform = ProfessionalSkillsForm(request.POST)
        if personform.is_valid() and educationform.is_valid() and professionalSkillsform.is_valid():
            person = personform.save()
            edu = educationform.save(commit=False)
            edu.person = person
            prof = professionalSkillsform.save(commit=False)
            prof.person = person
            educationform.save()
            professionalSkillsform.save()
            skills = prof.skill_detail
            l = skills.splitlines()[:4]
            context = {'person': person, 'prof': professionalSkillsform, 'edu': educationform, 'skills': l}
            return render(request, 'resume/resume_view.html', context)
    else:
        personform = PersonForm()
        educationform = EducationForm()
        professionalSkillsform = ProfessionalSkillsForm()

    return render(request, 'resume/resume_fill.html',
                  {'personform': personform, 'educationform': educationform,
                   "professionalSkillsform": professionalSkillsform})

