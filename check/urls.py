# check/urls.py

from django.urls import path
from .views import check, chart_data

urlpatterns = [
    path('', check, name='check'),  # 수정된 부분
    path('chart_data/', chart_data, name='chart_data'),  # 수정된 부분
]
