from django import forms
from .models import Report
from groups.models import GroupLinkProfessorSubject
from students.models import Student

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report 
        fields = ('id', 'group_1to1', 'student_1to1', 'subject_1to1', 'professor_1to1', 'skipped_days','document_pdf', )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #SHOWING  QUERYSET
        self.fields['student_1to1'].queryset = Student.objects.none()
        self.fields['subject_1to1'].queryset = GroupLinkProfessorSubject.objects.none()
        self.fields['professor_1to1'].queryset = GroupLinkProfessorSubject.objects.none()

        if 'group' in self.data:
            try:
                group_id = int(self.data.get('group_1to1'))
                self.fields['student_1to1'].queryset = Student.objects.filter(group_fk = group_id).order_by()
                self.fields['subject_1to1'].queryset = GroupLinkProfessorSubject.objects.filter(group_fk = group_id).order_by()
                self.fields['professor_1to1'].queryset = GroupLinkProfessorSubject.objects.filter(group_fk = group_id).order_by()
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty objects queryset
        
        elif self.instance.pk:
            self.fields['student_1to1'].queryset = self.instance.group_1to1.student_1to1_set
            self.fields['subject_1to1'].queryset = self.instance.group_1to1.subject_1to1_set
            self.fields['professor_1to1'].queryset = self.instance.group_1to1.professor_1to1_set
        
