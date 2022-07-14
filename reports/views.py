from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import Report
from students.models import Student
from .forms import ReportForm
from groups.models import GroupLinkProfessorSubject
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
    form_class = ReportForm
    template_name = 'report_new.html'
    success_url = reverse_lazy('report-list')

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