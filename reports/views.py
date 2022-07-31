from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from .models import Report
from students.models import Student
from .forms import ReportForm
from groups.models import GroupLinkProfessorSubject
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import ssl
from docxtpl import DocxTemplate
# Create your views here.

class ReportList(LoginRequiredMixin, ListView):
    model = Report
    context_object_name = 'report'
    template_name = "report_list.html"

class ReportDetail(DetailView):
    model = Report 
    context_object_name = 'report'
    template_name = "report_detail.html"
    success_url = reverse_lazy('report_list')


class ReportCreate(LoginRequiredMixin, CreateView):
    model = Report 
    form_class = ReportForm
    template_name = 'report_new.html'
    success_url = reverse_lazy('report_list')

def load_students(request):
    group_id = request.GET.get('group_1to1')
    students = Student.objects.filter(group_fk=group_id)
    return render(request, 'students_dropdown_list_options.html', {'students': students})

def load_subjects(request):
    group_id = request.GET.get('group_1to1')
    subjects = GroupLinkProfessorSubject.objects.filter(group_fk=group_id)
    return render(request, 'subjects_dropdown_list_options.html', {'subjects': subjects})

def load_professors(request):
    group_id = request.GET.get('group_1to1')
    professors = GroupLinkProfessorSubject.objects.filter(group_fk=group_id)
    return render(request, 'professors_dropdown_list_options.html', {'professors': professors})


def get_document(request, pk):
    doc = DocxTemplate("template.docx")
    url = f'http://127.0.0.1:8000/reports/{pk}/'

# Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    student_name = soup.find('div', class_='Student').p.text 
    group_name = soup.find('div', class_='Group').p.text 
    skipped_period = soup.find('div', class_='Skipped Period').p.text
    skipped_subject = soup.find('div', class_='Skipped Subject').p.text
    professor_name = soup.find('div', class_='Professor').p.text
    professor_email = soup.find('div', class_='Professor Email').p.text
    context = { 'student_name' : student_name, 'group_name' : group_name, 'period_date':skipped_period, 'professor_name' : professor_name, 'subject_name':skipped_subject}
    doc.render(context)
    doc.save(f"{student_name}__ID:{pk}.docx")
    return render(request, 'send_email.html', {'professor':professor_name, 'professor_email':professor_email})

