from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # path("", views.student_api),
    path("", views.StudentAPI.as_view()),
]
