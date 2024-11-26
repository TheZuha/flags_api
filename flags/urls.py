from django.urls import path
from .views import FlagsList, FlagsDetail

urlpatterns = [
    path('', FlagsList.as_view(), name="flags_list"),
    path('<int:pk>/', FlagsDetail.as_view(), name='flag_detail')
]