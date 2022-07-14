from django import forms
from .models import Report
from groups.models import Group
from students.models import Student
class ReportForm(forms.ModelForm):
    class Meta:
        model = Report 
        fields = ('id', 'group_1to1', 'student_1to1', 'subject_1to1', 'document_pdf')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student_1to1'].queryset = Student.objects.none()
        if 'group' in self.data:
            try:
                group_id = int(self.data.get('group_1to1'))
                self.fields['student_1to1'].queryset = Student.objects.filter(group_fk = group_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['student_1to1'].queryset = self.instance.group_1to1.student_1to1_set