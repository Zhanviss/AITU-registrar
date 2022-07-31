from django.urls import path
from .views import ReportList, ReportDetail, ReportCreate, load_students, load_subjects, load_professors, get_document
urlpatterns = [
    path('', ReportList.as_view(), name='report_list'),
    path('<int:pk>/', ReportDetail.as_view(), name='report_detail'),
    path('new/', ReportCreate.as_view(), name='report_new'),
    
    path('get-document/', get_document, name = 'get_document'),

    path('ajax/load-students/', load_students, name='ajax_load_students'),
    path('ajax/load-subjects/', load_subjects, name='ajax_load_subjects'),
    path('ajax/load-professors/', load_professors, name='ajax_load_professors'),
    
]