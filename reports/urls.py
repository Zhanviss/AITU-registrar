from django.urls import path
from .views import ReportList, ReportDetail, ReportCreate, ReportDelete, ReportUpdate,  load_students, load_subjects, load_professors, get_document, send_email
urlpatterns = [
    path('', ReportList.as_view(), name='report_list'),
    path('<int:pk>/', ReportDetail.as_view(), name='report_detail'),
    path('new/', ReportCreate.as_view(), name='report_new'),
    path('<int:pk>/delete/', ReportDelete.as_view(), name='report_delete'),
    path('<int:pk>/edit/', ReportUpdate.as_view(), name='report_update'),
    
    path('<int:pk>/document-generated', get_document, name = 'get_document'),
    path('<int:pk>/email-sent', send_email, name = 'send_email'),

    path('ajax/load-students/', load_students, name='ajax_load_students'),
    path('ajax/load-subjects/', load_subjects, name='ajax_load_subjects'),
    path('ajax/load-professors/', load_professors, name='ajax_load_professors'),
    
]