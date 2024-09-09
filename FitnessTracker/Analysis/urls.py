from django.urls import path
from Analysis import views
from Analysis.views import ReceiveDataView


urlpatterns = [
    path("", views.index, name="index"),
    path("api/data", ReceiveDataView.as_view(), name="receive_data")
]