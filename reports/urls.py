from django.urls import path
from .views import ReportList, ReportDetail, ReportCreate, load_students
urlpatterns = [
    path('', ReportList.as_view(), name='report-list'),
    path('<int:pk>/', ReportDetail.as_view(), name='report-detail'),
    path('new/', ReportCreate.as_view(), name='report-new'),

    path('ajax/load-students/', load_students, name='ajax_load_students'),
]