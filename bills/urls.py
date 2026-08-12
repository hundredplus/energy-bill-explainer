from django.urls import path
from .views import BillAnalysisView

urlpatterns = [
    path("analyse/", 
         BillAnalysisView.as_view(), 
         name="bill-analyse"),
]   