from django.urls import path
from .views import ReportList, ReportDetail, ReportCreate, load_students, load_subjects, load_professors
urlpatterns = [
    path('', ReportList.as_view(), name='report-list'),
    path('<int:pk>/', ReportDetail.as_view(), name='report-detail'),
    path('new/', ReportCreate.as_view(), name='report-new'),

    path('ajax/load-students/', load_students, name='ajax_load_students'),
    path('ajax/load-subjects/', load_subjects, name='ajax_load_subjects'),
    path('ajax/load-professors/', load_professors, name='ajax_load_professors'),
    
]