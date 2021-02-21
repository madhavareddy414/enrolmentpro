from django.urls import path

from django.conf.urls import url

from .views import StudentUpdateView
from register.views import home, stud_register, stud_all, stud_delete,stud_search,stud_detailView
urlpatterns = [
    path('index/', home),
    path('stud-reg/',stud_register,name='Student-Registration'),
    path('stud-update/<int:pk>/',StudentUpdateView.as_view()),
    path('stud-delete/',stud_delete,name='Student-deletion'),
    path('stud-all/',stud_all,name='Students-list'),
    path('stud-search/',stud_search,name='Students-search'),
    path('stud-detail/',stud_detailView,name='Student-detailview')

]
