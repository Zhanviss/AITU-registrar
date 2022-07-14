from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Report
from students.models import Student
# Create your views here.
#models.TextField(default=GroupLinkProfessorSubject.objects.all().filter(self.student_1to1.group_fk == GroupLinkProfessorSubject.group_fk).__str__())

class ReportList(ListView):
    model = Report
    template_name = "report_list.html"

class ReportDetail(DetailView):
    model = Report 
    template_name = "report_detail.html"

class ReportCreate(CreateView):
    model = Report 
    template_name = "report_new.html"
    fields = ('student_1to1', 'document_pdf')